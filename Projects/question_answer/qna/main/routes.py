from flask import Blueprint, redirect, render_template, request, url_for, session, abort
#from qna.db import get_db
from qna import db
from qna.users.utils import get_current_user
import datetime

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
@main_bp.route('/home')
def home():
    #db = get_db()
    try:
        db.execute(
            'SELECT * FROM questions WHERE answer_text IS NOT NULL')
        questions_ans = db.fetchall()

        db.execute('SELECT * FROM questions WHERE answer_text IS NULL')
        questions_no_ans = db.fetchall()

        db.execute(
            'SELECT username FROM users INNER JOIN questions ON users.id=questions.asked_by_id WHERE answer_text IS NULL')
        no_ans_asked_by = db.fetchall()

        db.execute(
            'SELECT username FROM users INNER JOIN questions ON users.id=questions.asked_by_id WHERE answer_text IS NOT NULL')
        ans_asked_by = db.fetchall()

        db.execute(
            'SELECT username FROM users INNER JOIN questions ON users.id=questions.expert_id')
        ans_answered_by = db.fetchall()

        ans_pretty_dates, no_ans_pretty_dates = [], []
        for i in range(len(questions_ans)):
            try:
                ans_pretty_dates.append(datetime.datetime.strptime(
                    str(questions_ans[i]['time']), '%Y-%m-%d %H:%M:%S').strftime('%B %d, %Y' + ' at ' + '%I:%M %p'))
            except Exception as e:
                raise abort("Error: " + str(e))

        for i in range(len(questions_no_ans)):
            try:
                no_ans_pretty_dates.append(datetime.datetime.strptime(
                    str(questions_no_ans[i]['time']), '%Y-%m-%d %H:%M:%S').strftime('%B %d, %Y' + ' at ' + '%I:%M %p'))
            except Exception as e:
                return "Error: " + str(e)

    except:
        abort(500)
    return render_template('home.html', questions_ans=questions_ans, questions_no_ans=questions_no_ans,
                           no_ans_asked_by=no_ans_asked_by, ans_asked_by=ans_asked_by,
                           no_ans_pretty_dates=no_ans_pretty_dates, ans_pretty_dates=ans_pretty_dates,
                           ans_answered_by=ans_answered_by)


@main_bp.route('/about')
def about():
    return render_template('about.html')
