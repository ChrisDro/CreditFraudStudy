from http.server import HTTPServer, BaseHTTPRequestHandler
import argparse
import os



class S(BaseHTTPRequestHandler):

    def do_GET(self):
        rootdir = os.getcwd() 
  
        try:
            print(rootdir + self.path)
            
            path = self.path.split("?",1)[0]
            if path == '/':
                self.path += 'home.html'   # default to home.html
                
            elif self.path.endswith('.html'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))  
                f.close()  
            elif self.path.endswith('.js'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header("Content-type", "application/javascript")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))  
                f.close()
            else:
                self.send_error(404, 'file not supported')  
                
        except IOError:
            self.send_error(404, 'file not found')  


    def do_POST(self):
        # Doesn't do anything with POST yet
       self.send_error(404, 'POST not supported')  
        

def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting server on {addr}:{port}")
    httpd.serve_forever()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
       "-l",
       "--listen",
       default="localhost",
       help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
       "-p",
       "--port",
       type=int,
       default=8000,
       help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)