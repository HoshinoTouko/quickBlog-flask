'''Archives module'''

import markdown
from flask import Blueprint, render_template
from ..model.db import DB

ARCHIVES = Blueprint('archives', __name__)

@ARCHIVES.route('/author/')
def archives_all_author():
    '''Show all author'''
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

@ARCHIVES.route('/author/')
def archives_author():
    '''Show all post of an author'''
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

@ARCHIVES.route('/<int:post_id>')
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
    '''Convert markdown to html'''
    return markdown.markdown(md)

