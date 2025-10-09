#!/usr/bin/python3
import http.server
import json

class MyServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            d = {"name": "John", "age": 30, "city": "New York"}
            js = json.dumps(d)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(js.encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            msg = {"status": "OK"}
            self.wfile.write(json.dumps(msg, separators=(',', ':')).encode())
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            inf = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(inf).encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    port = 8000
    serv = http.server.HTTPServer(("", port), MyServer)
    print("Server running on port", port)
    serv.serve_forever()
