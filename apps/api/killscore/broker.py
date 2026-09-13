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
        if q in _subs[run_id]:
            _subs[run_id].remove(q)


def publish(run_id: str, kind: str, data: dict) -> None:
    payload = json.dumps({"kind": kind, **data})
    with _lock:
        targets = list(_subs[run_id])
    for q in targets:
        q.put((kind, payload))
