from flask import render_template

from . import main
from ..new_word_notebook import get_random_new_word


@main.route('/new_word/random', methods=['GET'], endpoint='new_word_random')
def add():
    new_word = get_random_new_word()
    return render_template('english/new_word/random.html', new_word=new_word)
