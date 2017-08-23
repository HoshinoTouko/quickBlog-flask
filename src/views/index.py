'''Index view module'''

from flask import Blueprint, render_template, session

INDEX = Blueprint('index', __name__)

@INDEX.route('/')
def index():
    '''Do some stuff'''
    try:
        if session['username']:
            username = session['username']
    except BaseException:
        username = ''

    return render_template(
        'index/index.html',
        username=username
    )
