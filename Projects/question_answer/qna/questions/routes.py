from flask import Blueprint, redirect, render_template, request, url_for, session, flash, abort
from qna.db import get_db
import datetime

questions_bp = Blueprint('questions', __name__)


@questions_bp.route('/ask', methods=['GET', 'POST'])
def ask():

    if not session.get('id', None):
        abort(403)

    if request.method == "POST":
        db = get_db()
        question_text = request.form['question']

        db.execute('INSERT INTO questions (question_text, asked_by_id) VALUES(?, ?)', [
                   question_text, session['id']])
        db.commit()
        flash("Question asked successfully", "success")
        return redirect(url_for('main.home'))

    return render_template("ask.html")


@questions_bp.route('/answer', methods=['GET', 'POST'])
def answer():

    if session.get('expert', None) != 1:
        abort(403)

    db = get_db()
    questions_no_ans = db.execute(
        'SELECT * FROM questions WHERE answer_text IS NULL').fetchall()

    asked_by = db.execute(
        'SELECT username FROM users INNER JOIN questions ON users.id=questions.asked_by_id WHERE answer_text IS NULL').fetchall()

    pretty_dates = []
    for i in range(len(questions_no_ans)):
        pretty_dates.append(datetime.datetime.strptime(
            questions_no_ans[i]['time'], '%Y-%m-%d %H:%M:%S').strftime('%B %d, %Y' + ' at ' + '%I:%M %p'))

    return render_template('awaiting_questions.html', questions_no_ans=questions_no_ans, pretty_dates=pretty_dates, asked_by=asked_by)


@questions_bp.route('/answer/<int:id>', methods=['GET', 'POST'])
def answer_specific(id):

    if session.get('expert', None) != 1:
        abort(403)

    db = get_db()
    question = db.execute(
        'SELECT * FROM questions WHERE id=?', [id]).fetchone()

    asked_by = db.execute('SELECT username FROM users WHERE users.id=?', [
                          question['asked_by_id']]).fetchone()[0]

    if request.method == "POST":
        answer = request.form['answer']
        db.execute(
            'UPDATE questions SET answer_text=?, expert_id=? WHERE id=?', [answer, session['id'], question['id']])
        db.commit()
        flash("Answer submitted successfully", "success")
        return redirect(url_for('main.home'))

    return render_template('answer.html', question=question, asked_by=asked_by)
