'''Auth module(Like login/logout)'''

from flask import Blueprint, render_template, request, session, redirect, url_for

AUTH = Blueprint('auth', __name__)

@AUTH.route('/login', methods=['GET', 'POST'])
def login():
    '''Login func'''
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index.index'))

    try:
        if session['username']:
            return redirect(url_for('index.index'))
    except BaseException:
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@AUTH.route('/logout')
def logout():
    '''Log out func'''
    session.pop('username', None)
    return redirect(url_for('index.index'))
