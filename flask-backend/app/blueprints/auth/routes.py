from app.forms import RegisterForm, LoginForm
from app.blueprints.social.models import User, Post
from flask import Blueprint, render_template, redirect, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from . import auth_bp


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        check_username = User.query.filter_by(username=username).first()
        check_email = User.query.filter_by(email=email).first()
        if check_username:
            flash(f'Username {username} is taken, enter different Username')
            print("Username already exists")
        elif check_email:
            flash(f'Email {email} already in use, enter new email')
            print("Email already exists")
        else:
            u = User(username=username, email=email, password_hash='')
            u.hash_password(password)
            db.session.add(u)
            db.session.commit()
            login_user(u)
            flash(f'Register Requested for {email} {username}', 'success')
            print("User registered successfully")
            return redirect('/')
    else:
        print("Form not validated")
        print(form.errors)
    return render_template('register.jinja', form=form, title='Register')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash(f'{username} successfully signed in!')
            return redirect('/')
    return render_template('login.jinja', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
