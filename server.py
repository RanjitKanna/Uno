"""Color Clash local room server. Run: python server.py"""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import json, secrets, time

ROOT = Path(__file__).parent
ROOMS = {}

def code():
    return secrets.token_urlsafe(5).upper().replace("-", "A").replace("_", "B")[:6]

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def json(self, status, body):
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if not self.path.startswith("/api/"):
            return self.send_error(404)
        length = int(self.headers.get("Content-Length", 0))
        try:
            data = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            return self.json(400, {"error": "Invalid request."})
        action = self.path.rsplit("/", 1)[-1]
        if action == "create":
            capacity = data.get("capacity")
            name = str(data.get("name", "Host")).strip()[:20] or "Host"
            if capacity not in (2, 3, 4):
                return self.json(400, {"error": "Choose 2, 3, or 4 players."})
            room_code = code()
            while room_code in ROOMS: room_code = code()
            token = secrets.token_urlsafe(18)
            ROOMS[room_code] = {"capacity": capacity, "host": token, "players": [{"token": token, "name": name}], "started": False, "created": time.time()}
            return self.json(201, {"room": room_code, "token": token, "capacity": capacity})
        if action == "join":
            room_code = str(data.get("room", "")).upper().strip()
            name = str(data.get("name", "Guest")).strip()[:20] or "Guest"
            room = ROOMS.get(room_code)
            if not room: return self.json(404, {"error": "Room not found."})
            if room["started"]: return self.json(409, {"error": "This game has already started."})
            if len(room["players"]) >= room["capacity"]: return self.json(409, {"error": "This room is full."})
            token = secrets.token_urlsafe(18)
            room["players"].append({"token": token, "name": name})
            return self.json(200, {"room": room_code, "token": token, "capacity": room["capacity"]})
        if action == "start":
            room = ROOMS.get(str(data.get("room", "")).upper())
            if not room or data.get("token") != room["host"]: return self.json(403, {"error": "Only the host can start this room."})
            if len(room["players"]) < 2: return self.json(409, {"error": "Wait for at least one guest."})
            room["started"] = True
            return self.json(200, {"started": True})
        return self.json(404, {"error": "Unknown action."})

    def do_GET(self):
        if self.path.startswith("/api/state"):
            query = parse_qs(urlparse(self.path).query)
            room = ROOMS.get(query.get("room", [""])[0].upper())
            token = query.get("token", [""])[0]
            if not room or token not in {p["token"] for p in room["players"]}:
                return self.json(404, {"error": "Room not found."})
            return self.json(200, {"room": query["room"][0].upper(), "capacity": room["capacity"], "players": [{"name": p["name"]} for p in room["players"]], "isHost": token == room["host"], "started": room["started"]})
        super().do_GET()

if __name__ == "__main__":
    print("Color Clash server: http://localhost:8000")
    ThreadingHTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
