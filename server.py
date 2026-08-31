import http.server
import socketserver
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8055

class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Separate query string from path
        if '?' in self.path:
            clean_path, query = self.path.split('?', 1)
            query_str = '?' + query
        else:
            clean_path = self.path
            query_str = ''
        
        # Check if clean_path without extension maps to an existing .html file
        if clean_path != '/' and not os.path.splitext(clean_path)[1]:
            local_file = clean_path.lstrip('/') + '.html'
            if os.path.exists(local_file):
                self.path = clean_path + '.html' + query_str
                
        return super().do_GET()

# Multi-threaded server for fast non-blocking concurrent request handling
class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

if __name__ == '__main__':
    with ThreadedHTTPServer(("", PORT), CleanUrlHandler) as httpd:
        print(f"Serving Threaded HTTP with Clean URLs on port {PORT} (http://localhost:{PORT}/)...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
