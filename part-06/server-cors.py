#!/usr/bin/env python
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys

class RequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    test(RequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8080)
