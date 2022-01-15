# https://qiita.com/uchi_y/items/d5e2a89ee6ea51816d97

from flask import Flask, jsonify, request, abort
from setting import *
import signal, os, sys, datetime, time, string
import importlib
sys.path.append('./app/Controllers')
sys.path.append('./app/Services')

# 開発環境のみ
if setting['IS_LAMBDA'] == False:
    from flask_cors import CORS

# 以下controller読み込み
from TestController import *
from LoginController import *

app = Flask(__name__)

@app.after_request
def after_request(response):
    # 開発環境のみ
    if setting['IS_LAMBDA'] == False:
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

@app.route('/')
def root():
    controller = TestController()
    if request.method == 'GET':
        return controller.index()
    else:
        abort(404)

@app.route('/login')
def login():
    return LoginController().index()

@app.route('/test')
def test():
    return jsonify({"message": "test"})

@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def error_handler(error):
    '''
     Description
      - abort(400) / abort(404) / abort(500) した時にレスポンスをレンダリングするハンドラ
    '''
    return jsonify({ 'message': error.name, 'result': error.code }), error.code

if __name__ == '__main__':
    # debugモードtrueにしないと修正が反映されない
    app.run(debug=True, host='0.0.0.0', port=8080)

