#!/usr/bin/env python3
"""
Zero-dependency local HTTP development server for Akshat's Portfolio.
Supports directory index fallback, correct modern MIME types (woff2, webp, mp4),
and clean routing.
"""

import http.server
import socketserver
import os
import sys

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

PORT = int(os.environ.get("PORT", 3000))
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class PortfolioHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def guess_type(self, path):
        if path.endswith(".woff2"):
            return "font/woff2"
        if path.endswith(".woff"):
            return "font/woff"
        if path.endswith(".webp"):
            return "image/webp"
        if path.endswith(".mp4"):
            return "video/mp4"
        if path.endswith(".svg"):
            return "image/svg+xml"
        if path.endswith(".xml"):
            return "application/xml"
        return super().guess_type(path)

    def do_GET(self):
        # Strip caching request headers so browser always gets 200 OK fresh data
        for h in ["If-Modified-Since", "if-modified-since", "If-None-Match", "if-none-match"]:
            if h in self.headers:
                del self.headers[h]

        # Resolve clean paths like /projects/lific to /projects/lific/index.html
        url_path = self.path.split("?")[0].split("#")[0].strip("/")
        candidate = os.path.join(DIRECTORY, url_path)
        if os.path.isdir(candidate):
            index_path = os.path.join(candidate, "index.html")
            if os.path.exists(index_path) and not self.path.endswith("/"):
                self.send_response(301)
                self.send_header("Location", self.path + "/")
                self.end_headers()
                return

        return super().do_GET()

def run():
    handler = PortfolioHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("127.0.0.1", PORT), handler) as httpd:
            print("\n" + "=" * 50)
            print("⚡ Akshat's Portfolio Local Server is running!")
            print(f"📡 URL: http://127.0.0.1:{PORT}")
            print(f"📁 Serving directory: {DIRECTORY}")
            print("⌨️  Press Ctrl+C to stop.")
            print("=" * 50 + "\n")
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 98:
            alt_port = PORT + 1
            print(f"⚠️  Port {PORT} in use, trying {alt_port}...")
            os.environ["PORT"] = str(alt_port)
            with socketserver.TCPServer(("127.0.0.1", alt_port), handler) as httpd:
                print(f"📡 URL: http://127.0.0.1:{alt_port}")
                httpd.serve_forever()
        else:
            raise

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
