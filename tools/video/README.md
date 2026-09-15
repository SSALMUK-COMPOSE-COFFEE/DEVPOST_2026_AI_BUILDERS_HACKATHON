# Demo video and deck pipeline

```
cd tools/video && npm i playwright@1.49.1 && npx playwright install chromium
uv tool install edge-tts
python3 -c "import json,subprocess; [subprocess.run(['uvx','edge-tts','--voice','en-US-AndrewNeural','--rate','+3%','--text',t,'--write-media',f'tts/{k}.mp3']) for k,t in json.load(open('narration.json')).items()]"
REJ_RUN=<run id> REJ_MUTANT=<mutant id> node record.js
python3 build.py
node deck.js killscore-deck.pdf
```

`record.js` drives the live site scene by scene and writes one webm per scene. `build.py` pads each scene to its narration, burns captions, and concatenates. Everything on screen is the deployed product; nothing is pre-rendered except the four HTML title cards in `slides/`.
