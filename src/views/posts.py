'''Posts view module'''

import markdown
from flask import Blueprint, render_template
from ..model.db import DB

POSTS = Blueprint('posts', __name__)

@POSTS.route('/')
def posts_index():
    '''Post index'''
    database = DB()
    data = database.select('posts')
    # print(data)
    all_post_data = []
    for item in data:
        print(item)
        post_data = {
            'id': item[0],
            'title': item[1],
            'time': item[2],
            'text': md2html(item[3]),
            'labels': item[4].replace(';', ' '),
            'author': item[5]
        }
        all_post_data.append(post_data)
    return render_template(
        'posts/posts.html',
        all_post_data=all_post_data,
        title='Posts'
    )

@POSTS.route('/<int:post_id>')
def posts_detail(post_id):
    '''Post detail'''
    database = DB()
    data = database.select('posts')
    # print(data)
    for item in data:
        if item[0] == post_id:
            print(item)
            post_data = {
                'id': item[0],
                'title': item[1],
                'time': item[2],
                'text': md2html(item[3]),
                'labels': item[4].replace(';', ' '),
                'author': item[5]
            }
            return render_template(
                'posts/post.html',
                post_data=post_data,
                title=post_data['title']
            )
    return render_template('posts/post.html')


# Functions 
def md2html(md):
    return markdown.markdown(md)