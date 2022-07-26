from flask import Blueprint, request, redirect, render_template, url_for, session, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from qna.db import get_db
from qna.users.utils import get_current_user

users_bp = Blueprint('users', __name__)


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        db = get_db()

        username = request.form['username']
        password = request.form['password']

        user = db.execute(
            'SELECT * FROM users WHERE username = ?', [username]).fetchone()

        hashed_password = db.execute(
            'SELECT password FROM users WHERE username=?', [username]).fetchone()[0]
        if check_password_hash(hashed_password, password):
            session['username'] = user['id']
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


@users_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    username = session.pop('userarname', None)
    session.clear()
    if username:
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
            db.execute('INSERT INTO users (username, password, email, expert, admin) VALUES(?, ?, ?, 0, 0)',
                       [username, hashed_password, email])
            db.commit()
            flash('Successfully registered', 'success')
        except:
            flash('Registration failed, please try again with different values', 'danger')
    return render_template('register.html')


@users_bp.route('/users')
def users():
    db = get_db()
    users = db.execute('SELECT * FROM users WHERE admin=0').fetchall()
    admins = db.execute('SELECT * FROM users WHERE admin=1').fetchall()
    experts = db.execute('SELECT * FROM users WHERE expert=1').fetchall()
    return render_template('users.html', admins=admins, users=users, experts=experts)


@users_bp.route('/account/<int:id>')
def account(id):

    if session.get('id', None) != id:
        abort(403)
