'''A model for fetch or pull posts'''
import markdown
from .db import DB

# Get method
def get_all_posts_by_id(post_id):
    '''Get posts of one author'''
    return list_filter(get_all_posts(), 'id', post_id)

def get_all_posts_by_author(author):
    '''Get posts of one author'''
    return list_filter(get_all_posts(), 'author', author)

def get_all_posts():
    '''Get all posts from database'''
    database = DB()
    post_data = database.select('posts')
    all_post_data = []
    for item in post_data:
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
    return all_post_data

# Functions

def list_filter(original_list, key, value):
    '''A filter for filtering key and value'''
    result = []
    for item in original_list:
        if item[key] == value:
            result.append(item)
    return result

def md2html(markdown_text):
    '''Convert markdown to html'''
    return markdown.markdown(markdown_text)
