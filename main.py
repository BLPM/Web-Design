import os
from flask import Flask, request, render_template
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




port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(threaded=True, host='127.0.0.1', port=port)
