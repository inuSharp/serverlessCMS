from flask import Flask, jsonify

from setting      import *

app = Flask(__name__)

@app.route('/')
def root():
    data = {
        "id": setting['DB_HOST'],
        "name": "hoge4",
        "ref": [1, 2, 4],
    }
    return jsonify(data)

@app.route('/test')
def test():
    return jsonify({"message": "test"})

if __name__ == '__main__':
    # debugモードtrueにしないと修正が反映されない
    app.run(debug=True, host='0.0.0.0', port=80)

