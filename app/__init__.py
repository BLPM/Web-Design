import os
from flask import Flask,render_template, request,jsonify,redirect,url_for,flash
from flask_login import LoginManager
from flask_migrate import Migrate

from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from .model.user_model import User,db
from .view.auth import auth



LogInManager = LoginManager()
migrate = Migrate()

def create_app():
    app  = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdjaslgdflgmgfsadgl'   
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://pc:Au4a831j4_cl3j06@192.168.182.134:3306/webPractice"

    app.register_blueprint(auth)
    migrate.init_app(app,db)
    db.init_app(app)

    LogInManager.init_app(app)
    LogInManager.session_protection = "strong"

#   @app.route('/create_dataBase')
#    def creat_cb():
#        db.create_all()
#        return 'ok'


    @LogInManager.user_loader  
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))


    @app.route("/", methods=['GET'])
    def index():
        if request.method == "GET":
            return render_template("index.html")
        

    @app.route("/BrainPower",methods=['POST'])
    def asree():
        return 

    @app.route('/hello/<username>')
    def hello(username):
        return render_template('hello.html', username=username)

    return app



