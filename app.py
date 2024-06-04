from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/items', methods=['GET'])
def get_items():
    items = [
        {'id': 1, 'name': 'Item 1', 'description': 'Description 1'},
        {'id': 2, 'name': 'Item 2', 'description': 'Description 2'},
    ]
    return jsonify(items)

if __name__ == '__main__':
    app.run()
