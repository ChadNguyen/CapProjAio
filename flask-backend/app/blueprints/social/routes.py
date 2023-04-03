from . import bp as social_bp
from ...blueprints.social.models import Post, User
from app.forms import PostForm
from flask import render_template, flash, redirect, url_for, current_app
from flask_login import current_user, login_required
from app import db


@social_bp.route('/user/<username>')
def user(username):
    with current_app.app_context():
        user_match = User.query.filter_by(username=username).first()
        if not user_match:
            redirect('/')
        posts = user_match.posts
    return render_template('user.jinja', user=user_match, posts=posts)


@social_bp.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        body = form.body.data
        p = Post(body=body, user_id=current_user.id)
        with current_app.app_context():
            db.session.add(p)
            db.session.commit()
        return redirect(url_for('social.user', username=current_user.username))
    return render_template('post.jinja', post_form=form)
