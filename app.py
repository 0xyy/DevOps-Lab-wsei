from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<h1>Witaj w DevOps Lab!</h1><p>To dziala na Dockerze/Pythonie</p>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer(("0.0.0.0", 8080), SimpleServer)
    print("Serwer wystartowal na porcie 8080...")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
