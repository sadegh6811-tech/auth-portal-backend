import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

class MockBackend(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        # این خط به دامنه Vercel اجازه دسترسی می‌دهد
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(200)

    def do_GET(self):
        if self.path == '/api/market':
            response = {"success": True, "data": [{"symbol": "BTCUSDT", "price": 65000.5}, {"symbol": "ETHUSDT", "price": 3500.2}]}
        else:
            response = {"status": "ok", "message": "Cloud Backend is running"}
        self._set_headers(200)
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        _ = self.rfile.read(content_length)
        
        if self.path == '/api/auth/login' or self.path == '/api/auth/register':
            response = {"access_token": "mock_token_12345", "token_type": "bearer", "user": "sadegh"}
        elif self.path == '/api/karami/trade':
            response = {"success": True, "log": ">> KARAMI ENGINE v2.0 (CLOUD)...\n>> SUCCESS. 3 TRADES COMPLETED."}
        elif self.path == '/api/mathbot/discover':
            response = {"success": True, "log": ">> MATHBOT DISCOVERY (CLOUD)...\n>> FOUND NEW EQUATION: E = mc^2"}
        else:
            response = {"success": True, "message": "Cloud endpoint reached"}
        
        self._set_headers(200)
        self.wfile.write(json.dumps(response).encode('utf-8'))

port = int(os.environ.get("PORT", 8000))
print(f"🚀 Cloud Backend running on port {port}")
ThreadingHTTPServer(('0.0.0.0', port), MockBackend).serve_forever()
