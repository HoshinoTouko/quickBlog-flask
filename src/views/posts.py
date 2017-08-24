'''Posts module'''

from flask import Blueprint, render_template
from ..model import postModel

POSTS = Blueprint('posts', __name__)

@POSTS.route('/')
def posts_index():
    '''Post index'''
    all_post_data = postModel.get_all_posts()
    # print(all_post_data)
    return render_template(
        'posts/posts.html',
        all_post_data=all_post_data,
        title='Posts'
    )

@POSTS.route('/<int:post_id>')
def posts_detail(post_id):
    '''Post detail'''
    try:
        post_data = postModel.get_post_by_id(post_id)[0]
        return render_template(
            'posts/post.html',
            post_data=post_data,
            title=post_data['title']
        )
    except BaseException:
        return render_template('posts/post.html')
