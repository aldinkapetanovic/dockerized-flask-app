import sys
import socket
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    python_version = sys.version.split()[0]
    return f'''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{hostname}</title>

        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                display: flex;
                align-items: center;
                justify-content: center;
                flex-direction: column;
                height: 100vh;
                background-color: #f8f9fa;
            }}

            h1 {{
                font-size: 5vw;
                color: #007bff;
                margin: 0;
            }}

            p {{
                font-size: 1.5em;
                margin-top: 10px;
                color: #6c757d;
            }}

            .highlight {{
                font-size: 0.8em;
                font-family: monospace;
                background-color: #f0f0f0;
                padding: 5px;
                border-radius: 4px;
            }}
        </style>
    </head>

    <body>
        <div>
            <p>Hi, my name is <span class="highlight">{hostname}!</span> 🐳</p>
            <p>Python Version: <span class="highlight">{python_version}</span> 🚀</p>
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
