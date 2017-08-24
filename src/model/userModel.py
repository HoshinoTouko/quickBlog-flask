'''A model for user functions'''
from .db import DB

def auth_user_and_pass(username, password):
    '''Auth user by name and pass'''
    data = get_all_users()
    for item in data:
        if item['name'] == username and item['pass'] == password:
            return True
    return False

def get_all_users():
    '''Get all posts from database'''
    database = DB()
    post_data = database.select('auth')
    all_post_data = []
    for item in post_data:
        print(item)
        post_data = {
            'id': item[0],
            'name': item[1],
            'pass': item[2]
        }
        all_post_data.append(post_data)
    return all_post_data
