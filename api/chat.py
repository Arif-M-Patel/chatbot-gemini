from http.server import BaseHTTPRequestHandler
import json
import os
from google import genai
from google.genai import types

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Read request body
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            message = data.get('message', '')
            
            if not message:
                self.send_error(400, 'Message is required')
                return
            
            # Get API key from environment
            api_key = os.environ.get('GEMINI_API_KEY')
            if not api_key:
                self.send_error(500, 'API key not configured')
                return
            
            # Initialize Gemini client
            client = genai.Client(api_key=api_key)
            
            # Generate response
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=message,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(thinking_budget=0)
                )
            )
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response_data = {
                'response': response.text
            }
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {
                'error': str(e)
            }
            self.wfile.write(json.dumps(error_response).encode('utf-8'))
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps({"status": "Server is running"}).encode("utf-8"))

if __name__ == "__main__":
        from http.server import HTTPServer
        import os

        port = int(os.environ.get("PORT", 8000))
        server_address = ("", port)
        httpd = HTTPServer(server_address, handler)
        print(f"Server running at http://localhost:{port}")
        httpd.serve_forever()