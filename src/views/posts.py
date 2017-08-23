'''Posts view module'''

from flask import Blueprint, render_template

POSTS = Blueprint('posts', __name__)

@POSTS.route('/')
def posts_index():
    '''Do some stuff'''
    return render_template('posts/posts.html')
