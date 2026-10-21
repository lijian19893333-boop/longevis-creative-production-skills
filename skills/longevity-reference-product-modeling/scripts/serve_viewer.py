#!/usr/bin/env python3
"""Serve a copied viewer directory on localhost, with fresh model responses."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def list_directory(self, path):
        self.send_error(403, 'Directory listing disabled')
        return None


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', required=True, type=Path)
    parser.add_argument('--port', type=int, default=0, help='0 selects a free port; reuse a known free port for a stable project URL')
    args=parser.parse_args()
    directory=args.directory.expanduser().resolve()
    if not (directory/'index.html').is_file():
        parser.error('directory must contain the copied viewer index.html')
    if not 0 <= args.port <= 65535:
        parser.error('port must be between 0 and 65535')
    try:
        server=ThreadingHTTPServer(('127.0.0.1',args.port),partial(Handler,directory=str(directory)))
    except OSError as error:
        parser.exit(2,f'Cannot start local viewer: {error}\n')
    print(f'http://127.0.0.1:{server.server_port}/index.html',flush=True)
    print('Keep this process running. Press Ctrl+C to stop.',flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

if __name__=='__main__':
    main()
