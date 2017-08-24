'''Archives module'''

import markdown
from flask import Blueprint, render_template
from ..model.db import DB
from ..model import postModel

ARCHIVES = Blueprint('archives', __name__)

@ARCHIVES.route('/author/')
def archives_all_author():
    '''Show all author'''
    all_post_data = postModel.get_all_posts()
    author_data = {}
    # author_data maybe like this: {author1: [posts], author2: [posts]}
    for item in all_post_data:
        if item['author'] not in author_data.keys():
            author_data[item['author']] = []
        author_data[item['author']].append(item)
    print(author_data)
    return render_template(
        'archives/authors.html',
        author_data=author_data,
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

