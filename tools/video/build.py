import json
import re
import subprocess
import sys
from pathlib import Path

V = Path(__file__).parent
ORDER = ["hook", "intro", "live", "survivor", "rejected", "arch", "evals", "gate", "end"]
LEAD = {"hook": 0.4, "live": 0.8, "survivor": 0.5, "rejected": 0.3, "gate": 0.5}
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def dur(p: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout.strip()
    return float(out)


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.?!])\s+", text.strip())
    out = []
    for p in parts:
        while len(p) > 95:
            cut = p.rfind(" ", 0, 95)
            out.append(p[:cut])
            p = p[cut + 1 :]
        out.append(p)
    return out


def srt_for(text: str, audio_len: float, offset: float) -> list[tuple[float, float, str]]:
    sents = sentences(text)
    weights = [len(s) for s in sents]
    total = sum(weights)
    t = offset
    cues = []
    for s, w in zip(sents, weights):
        d = audio_len * w / total
        cues.append((t, t + d, s))
        t += d
    return cues


def fmt(t: float) -> str:
    h = int(t // 3600)
    m = int(t % 3600 // 60)
    s = t % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")


def main(names: list[str]) -> None:
    narration = json.loads((V / "narration.json").read_text())
    (V / "seg").mkdir(exist_ok=True)
    segs = []
    cues = []
    clock = 0.0
    for name in names:
        video = V / "rec" / f"{name}.webm"
        audio = V / "tts" / f"{name}.mp3"
        vlen, alen = dur(video), dur(audio)
        lead = LEAD.get(name, 0.2)
        total = max(vlen, alen + lead + 0.6)
        seg = V / "seg" / f"{name}.mp4"
        cmd = [
            "ffmpeg", "-y", "-v", "error",
            "-i", str(video), "-i", str(audio),
            "-filter_complex",
            f"[0:v]fps=30,scale=1920:1080:flags=lanczos,tpad=stop_mode=clone:stop_duration=60,trim=duration={total:.3f},setpts=PTS-STARTPTS[v];"
            f"[1:a]adelay={int(lead*1000)}|{int(lead*1000)},apad,atrim=duration={total:.3f},asetpts=PTS-STARTPTS[a]",
            "-map", "[v]", "-map", "[a]",
            "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "160k", "-ar", "44100",
            str(seg),
        ]
        subprocess.run(cmd, check=True)
        segs.append(seg)
        cues += srt_for(narration[name], alen, clock + lead)
        print(f"{name:<9} video {vlen:5.1f}s  audio {alen:5.1f}s  -> {total:5.1f}s  (t={clock:.1f})")
        clock += total

    srt = V / "captions.srt"
    srt.write_text("".join(f"{i}\n{fmt(a)} --> {fmt(b)}\n{t}\n\n" for i, (a, b, t) in enumerate(cues, 1)))
    (V / "concat.txt").write_text("".join(f"file '{s}'\n" for s in segs))
    raw = V / "killscore-raw.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(V / "concat.txt"), "-c", "copy", str(raw)], check=True)
    final = V / "killscore-demo.mp4"
    style = "FontName=DejaVu Sans,FontSize=10,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00101010,BorderStyle=1,Outline=1.6,Shadow=0.8,MarginV=26,Alignment=2"
    subprocess.run([
        "ffmpeg", "-y", "-v", "error", "-i", str(raw),
        "-vf", f"subtitles={srt}:force_style='{style}'",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart",
        str(final),
    ], check=True)
    print(f"total {clock:.1f}s -> {final}")


if __name__ == "__main__":
    main(sys.argv[1:] or ORDER)
