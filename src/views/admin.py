'''Auth module(Like login/logout)'''

from functools import wraps
from flask import Blueprint, render_template, request, session, redirect, url_for
from ..model import userModel

ADMIN = Blueprint('admin', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_login():
            return redirect(url_for('admin.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def is_login():
    '''Check if the user has login'''
    if 'isLogin' in session.keys():
        if session['isLogin']:
            return True
    return False

@ADMIN.route('/')
@login_required
def index():
    '''Log out func'''
    return render_template('admin/index.html')

@ADMIN.route('/login', methods=['GET', 'POST'])
def login():
    '''Login func'''
    if is_login():
        return redirect(url_for('admin.index'))

    if request.method == 'POST':
        if userModel.auth_user_and_pass(request.form['username'], request.form['password']):
            session['username'] = request.form['username']
            session['isLogin'] = True
            return redirect(url_for('admin.index'))
        else:
            return render_template('admin/login.html', tips='Wrong username or password!')
    return render_template('admin/login.html')

@ADMIN.route('/logout')
def logout():
    '''Log out func'''
    session.pop('username', None)
    session['isLogin'] = False
    return redirect(url_for('admin.login'))
