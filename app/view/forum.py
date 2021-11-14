from flask import Blueprint ,request,render_template ,flash ,redirect,url_for,abort
from flask_login import login_user,login_required,logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..model.user_model import User ,db


forum = Blueprint('forum', __name__)


@forum.route("/ask", methods=['GET', 'POST'])
def AskPage():
    if request.method == "GET":
        return render_template("forum.html")
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))
        login_user(user, remember=remember)

        return redirect(url_for('hello', username=user.username ))