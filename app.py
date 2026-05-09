import sys
import socket
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    python_version = sys.version.split()[0]
    # client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{hostname}</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                margin: 0;
                padding: 2rem;
                background: #f8f9fa;
                color: #111;
            }}
            .card {{
                max-width: 700px;
                margin: 0 auto;
                padding: 2rem;
                background: white;
                border-radius: 16px;
                box-shadow: 0 14px 40px rgba(15, 23, 42, 0.08);
            }}
            h1 {{
                margin-top: 0;
                color: #0d6efd;
            }}
            p {{
                line-height: 1.7;
                margin: .8rem 0;
            }}
            .highlight {{
                display: inline-block;
                padding: 0.25rem 0.5rem;
                background: #f1f5ff;
                border-radius: 6px;
                font-family: Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;
                color: #0b3d91;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello from Flask</h1>
            <p>Hostname: <span class="highlight">{hostname}</span></p>
            <p>Python version: <span class="highlight">{python_version}</span></p>
            <!-- <p>Client IP: <span class="highlight">{client_ip}</span></p> -->
            <p>Try <code>/items</code> to see JSON API output.</p>
        </div>
    </body>
    </html>
    '''

@app.route('/items', methods=['GET'])
def get_items():
    items = [
        {'id': 1, 'name': 'Item 1', 'description': 'Description 1'},
        {'id': 2, 'name': 'Item 2', 'description': 'Description 2'},
    ]
    return jsonify(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
