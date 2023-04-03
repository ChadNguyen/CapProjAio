# from flask import Blueprint, render_template, redirect, flash, url_for
# from app.forms import RegisterForm, LoginForm
# from app.blueprints.social.models import User, Post
# from flask_login import current_user, login_user, logout_user, login_required
# from app import app


# bp = Blueprint('auth', __name__, url_prefix='/auth')

# @bp.route('/')
# def index():
#     return render_template('index.jinja', title='Home')

# @bp.route('/about')
# def about():
#     return render_template('about.jinja')

# @bp.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         email = form.email.data
#         password = form.password.data
        
#         check_username = User.query.filter_by(username=username).first()
#         check_email = User.query.filter_by(email=email).first()
#         if check_username:
#             flash(f'Username {username} is taken, enter different Username')
#         elif check_email:
#             flash(f'Email {email} already in use, enter new email')
#         else:
#             u = User(username=username,email=email,password_hash='')
#             u.hash_password(password)
#             print(u.password_hash)
#             u.commit()
#             login_user(u)
#             flash(f'Register Requested for {email} {username}','success')
#             return redirect('/')
#     return render_template('register.jinja', form=form, title='Register')

# @bp.route('/login', methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data
#         user = User.query.filter_by(username=username).first()
#         if user and user.check_password(password):
#             login_user(user)
#             flash(f'{username} successfully signed in!')
#             return redirect('/')
#     return render_template('login.jinja', sign_in_form=form)

# @bp.route('/logout')
# def log_out():
#     logout_user()
#     return redirect(url_for('main.index'))
