from email.policy import default
from flask import Blueprint, request, redirect, render_template, url_for, session, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from qna.db import get_db
from qna.users.utils import get_current_user
import time

users_bp = Blueprint('users', __name__)


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        db = get_db()

        username = request.form['username']
        password = request.form['password']

        db.execute(
            'SELECT * FROM users WHERE username = %s', (username,))
        user = db.fetchone()

        if user is None:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('users.login'))

        db.execute(
            'SELECT password FROM users WHERE username=%s', (username,))
        hashed_password = db.fetchone()[0]
        if check_password_hash(hashed_password, password):
            session['username'] = user['username']
            session['id'] = user['id']
            session['email'] = user['email']
            session['admin'] = user['admin']
            session['expert'] = user['expert']

            flash('Successfully logged in', 'success')
        else:
            flash('Incorrect username or password', 'danger')

    if session.get('id', None):
        return redirect(url_for('main.home'))
    return render_template('login.html')


@users_bp.route('/logout/<int:updated>', methods=['GET', 'POST'])
def logout(updated=0):
    print(updated)

    username = session.pop('username', None)
    session.clear()
    referrer = request.referrer

    if username:

        if 'account' in referrer and updated == 1:
            flash(
                'Successfully updated account credentials. Please log in again.', 'success')
            return redirect(url_for('users.login'))
        else:
            flash('Successfully logged out', 'success')
    return redirect(url_for('main.home'))


@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('id', None):
        return redirect(url_for('main.home'))

    if request.method == "POST":
        db = get_db()
        username = request.form['username']
        hashed_password = generate_password_hash(
            request.form['password'], method='sha256')
        email = request.form['email']
        try:
            db.execute(
                'SELECT * FROM users WHERE username = %s', (username,))
            username_exists = db.fetchone()
            if username_exists:
                flash('Username already exists', 'danger')
                raise Exception('Username already exists')

            db.execute('INSERT INTO users (username, password, email, expert, admin) VALUES(%s, %s, %s, FALSE, FALSE)',
                       (username, hashed_password, email,))

            flash('Successfully registered', 'success')
        except:
            flash('Registration failed, please try again with different values', 'danger')
    return render_template('register.html')


@users_bp.route('/users')
def users():
    db = get_db()
    db.execute('SELECT * FROM users WHERE admin=FALSE')
    users = db.fetchall()

    db.execute('SELECT * FROM users WHERE admin=TRUE')
    admins = db.fetchall()

    db.execute('SELECT * FROM users WHERE expert=TRUE')
    experts = db.fetchall()
    return render_template('users.html', admins=admins, users=users, experts=experts)


@users_bp.route('/account/<int:id>', methods=['GET', 'POST'])
def account(id):
    if session.get('id', None) != id:
        abort(403)

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        try:
            db = get_db()
            db.execute('SELECT * FROM users WHERE id = %s', (id,))
            curr_user = db.fetchone()

            db.execute('SELECT * FROM users WHERE username = %s', (username,))
            new_username = db.fetchone()
            if new_username != None and new_username['id'] != id:
                flash('New username already exists', 'danger')
                return redirect(url_for('users.account', id=id))

            db.execute('SELECT * FROM users WHERE email = %s', (email,))
            new_email = db.fetchone()
            if new_email != None and new_email['email'] != curr_user['email']:
                flash('New email already exists', 'danger')
                return redirect(url_for('users.account', id=id))

            if(len(password) > 0):
                password = generate_password_hash(
                    password, method='sha256')
            else:
                password = curr_user['password']

            db.execute('UPDATE users SET username = %s, password = %s, email = %s WHERE id = %s',
                       (username, password, email, id,))

            return redirect(url_for('users.logout', updated=1))

        except Exception as e:
            return e, 500

    return render_template('account.html')
