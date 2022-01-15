import signal, os, sys, re, datetime, time, string, random
from flask import jsonify

from LoginService import *

class LoginController:
    # def __init__(self):

    def index(self):
        service = LoginService()
        data = service.index()
        return jsonify(data)

