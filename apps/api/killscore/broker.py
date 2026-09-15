import json
import queue
import threading
from collections import defaultdict

_subs: dict[str, list[queue.Queue]] = defaultdict(list)
_lock = threading.Lock()


def subscribe(run_id: str) -> queue.Queue:
    q: queue.Queue = queue.Queue()
    with _lock:
        _subs[run_id].append(q)
    return q


def unsubscribe(run_id: str, q: queue.Queue) -> None:
    with _lock:
        subs = _subs.get(run_id)
        if subs is None:
            return
        if q in subs:
            subs.remove(q)
        if not subs:
            del _subs[run_id]


def publish(run_id: str, kind: str, data: dict) -> None:
    payload = json.dumps({"kind": kind, **data})
    with _lock:
        targets = list(_subs.get(run_id, ()))
    for q in targets:
        q.put((kind, payload))
