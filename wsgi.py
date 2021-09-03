import os
from flask import Flask, request, render_template,jsonify
import requests
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    if request.method == "GET":
        return render_template("index.html")
        
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
@app.route("/BrainPower",methods=['POST'])
def te():
    C8763 = {
        'name':"游凱輝",
        'song':"Aribuda",
        'password':""
        }
    return jsonify(C8763) 


port = int(os.environ.get('PORT', 8001))
if __name__ == '__main__':
    app.run(threaded=True, host='127.0.0.1', port=port)
