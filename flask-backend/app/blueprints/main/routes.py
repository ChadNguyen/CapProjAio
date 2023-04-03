from flask import Blueprint, render_template, jsonify
from app.forms import SearchForm, PostForm
from app.games.animal_dices import play_animal_dices

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    form = SearchForm()
    form2 = PostForm()
    return render_template('index.jinja', title='Home', search_form=form, post_form=form2)

@main_bp.route('/about')
def about():
    form = SearchForm()
    form2 = PostForm()
    return render_template('about.jinja', search_form=form, post_form=form2)

@main_bp.route('/game1')
def AnimalDices():
    result_str = play_animal_dices(emoji_mode=True)
    return render_template('animaldices.jinja', result_str=result_str)

@main_bp.route('/roll_dice')
def roll_dice():
    result_str = play_animal_dices(emoji_mode=False, roll=True)
    return jsonify({'result_str': result_str})

# connect react to backend should display together now. maybe
@main_bp.route('/react-app/')
def serve_react_app():
    return render_template('react_app.html')





