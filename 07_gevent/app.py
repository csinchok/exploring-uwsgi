import gevent
from gevent import queue
import collections
import time
from urllib.parse import parse_qs
import base64
GIF_DATA = base64.b64decode("R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==")

event_queue = queue.Queue()


def count_events():
    while True:
        gevent.sleep(1)
        counter = collections.Counter()

        now = int(time.time())

        while True:
            try:
                event = event_queue.get_nowait()
            except queue.Empty:
                break
            counter[event] += 1

        if len(counter):
            lines = []

            for key, value in counter.items():
                lines.append("** {} {} {}  **".format(key, value, now))

            message = "\n".join(lines) + "\n"
            print(message)

gevent.spawn(count_events)


def tracker(env, start_response):
    if env["PATH_INFO"] == "/track.gif":
        start_response("200 OK", [("Content-Type", "image/gif")])
        yield GIF_DATA

        parsed = parse_qs(env["QUERY_STRING"])

        events = parsed.get("event", [])
        for event in events:
            event_queue.put(event)
    else:
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        yield "Nothing here."
