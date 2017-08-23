'''Posts view module'''

import markdown
from flask import Blueprint, render_template
from ..model.db import DB

POSTS = Blueprint('posts', __name__)

@POSTS.route('/')
def posts_index():
    '''Post index'''
    return render_template('posts/posts.html')

@POSTS.route('/<int:post_id>')
def posts_detail(post_id):
    '''Post detail'''
    database = DB()
    data = database.select('posts')
    # print(data)
    for item in data:
        if item[0] == post_id:
            print(item)
            postdata = {
                'id': item[0],
                'title': item[1],
                'time': item[2],
                'text': md2html(item[3]),
                'label': item[4].replace(';', ' '),
                'author': item[5]
            }
            return render_template('posts/post.html', postdata=postdata)
    return render_template('posts/post.html')


# Functions 
def md2html(md):
    return markdown.markdown(md)