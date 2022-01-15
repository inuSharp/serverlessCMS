import signal, os, sys, re, datetime, time, string, random
from flask import jsonify
from setting      import *

# from LoginService import *

class TestController:
    # def __init__(self):

    def index(self):
        data = {
            "id": setting['IS_LAMBDA'],
            "name": "hoge4",
            "ref": [1, 2, 4],
        }
        return jsonify(data)

