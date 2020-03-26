from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, SignInForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username = form.username.data, password = form.password.data).first()
   
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")
    
    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/sign", methods = ["GET", "POST"])
def auth_sign_in():
    if request.method == "GET":
        return render_template("auth/signinform.html", form = SignInForm())

    form = SignInForm(request.form)

    user = User.query.filter_by(username = form.username.data).first()

    if user:
        return render_template("auth/signinform.html", form = form,
                                error = "Username is already used")

    a = User(form.name.data, form.username.data, form.password.data)

    db.session.add(a)
    db.session.commit()

    return render_template("auth/loginform.html", form = LoginForm())