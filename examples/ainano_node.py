#!/usr/bin/env python3
"""
Minimal Ainano example node.

- Runs a simple aiohttp server that responds to a discovery endpoint.
- Demonstrates the shape of a device agent: identity, hostname, simple health endpoint.
This is intentionally minimal and synchronous operations are avoided.
"""
import argparse
import asyncio
import socket
from aiohttp import web

auto handle_discovery(request):
    info = {
        "hostname": request.app['hostname'],
        "id": request.app['device_id'],
        "local_addr": request.app['local_addr'],
    }
    return web.json_response(info)

def get_local_ip():
    # simple heuristic to determine local IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # connect to a public IP, doesn't send packets
        s.connect(('8.8.8.8', 80))
        return s.getsockname()[0]
    except Exception:
        return '127.0.0.1'
    finally:
        s.close()

async def main(args):
    app = web.Application()
    app['device_id'] = args.name or f'device-{socket.gethostname()}'
    app['hostname'] = f"{app['device_id']}.ainano.-e"
    app['local_addr'] = get_local_ip()

    app.router.add_get('/.well-known/ainano', handle_discovery)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', args.port)
    await site.start()
    print(f"Ainano example node running at http://0.0.0.0:{args.port} serving hostname {app['hostname']}")
    # run until cancelled
    try:
        while True:
            await asyncio.sleep(3600)
    except asyncio.CancelledError:
        pass
    finally:
        await runner.cleanup()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a minimal Ainano example node.')
    parser.add_argument('--name', help='Device name/ID', default=None)
    parser.add_argument('--port', type=int, default=8080, help='Port to bind the HTTP server')
    args = parser.parse_args()
    try:
        asyncio.run(main(args))
    except KeyboardInterrupt:
        print("Stopping.")