from flask import Blueprint ,request,render_template ,flash ,redirect,url_for,abort
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..model.user_model import User ,db


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))
        login_user(user, remember=remember)
        return 'you\'re login'


@auth.route("/signup",methods = ['GET','POST'])
def sign():
    if request.method=='GET':
        return render_template("signup.html")

    if request.method=='POST':
        name = request.form.get('name')
        email= request.form.get('email')
        password = request.form.get('password')
        user= User.query.filter_by(email=email).first()
        if user:
            return redirect(url_for("index"))
        new_user = User(email=email,username=name, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
