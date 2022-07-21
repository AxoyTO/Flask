from flask import Blueprint, redirect, request, render_template, url_for
from foodtracker.db import get_db
import datetime

dates_bp = Blueprint('dates', __name__)

@dates_bp.route('/dates/<string:date>', methods=['GET', 'POST'])
def date(date):
    db = get_db()
    foods = db.execute('SELECT * FROM food').fetchall()
    pretty_date = date
    
    pretty_date = datetime.datetime.strptime(date,'%Y%m%d').strftime('%B %d, %Y')
    date_res = db.execute('SELECT id, entry_date from log_date WHERE entry_date = ?', [date]).fetchone()
    
    if request.method=='POST':
        food = request.form['foods']
        food = db.execute('SELECT * FROM food WHERE name=?', [food]).fetchone()
        db.execute('INSERT INTO food_date (food_id, log_date_id) values (?, ?)', [food['id'],date_res['id'] ])
        db.commit()
        
    

    total_foods = db.execute('SELECT id, food_id FROM food_date WHERE log_date_id = ?', [date_res['id']]).fetchall()
    
    cals, protein, fat, carbs = 0,0,0,0
    ids=[]
    for i in total_foods:
        ids.append(i['id'])
        for j in db.execute('SELECT * FROM food WHERE id=?', [i['food_id']]).fetchall():
            cals += j['calories']
            protein += j['protein']
            fat += j['fat']
            carbs += j['carbohydrates']
    
    total_foods = [db.execute('SELECT * FROM food WHERE id=?', [i['food_id']]).fetchone() for i in total_foods]
    
    return render_template('date.html', date=pretty_date, foods=foods, total_foods=total_foods, ids=ids,\
        total_cals=cals, total_protein=protein, total_fat=fat, total_carbs=carbs, e=enumerate(total_foods))


@dates_bp.route('/dates/food_delete/<string:date>/<int:id>', methods=['GET', 'POST'])
def food_delete(date, id):
    db = get_db()
    db.execute('DELETE FROM food_date WHERE id=?', [id])
    db.commit()
    
    date = datetime.datetime.strptime(date,'%B %d, %Y').strftime('%Y%m%d')
    return redirect(url_for('dates.date', date=date))
