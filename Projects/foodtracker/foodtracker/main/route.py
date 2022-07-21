from crypt import methods
from typing import final
from flask import Blueprint, render_template, redirect, url_for, request
import datetime
from foodtracker.db import get_db

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
@main_bp.route('/home', methods=['GET', 'POST'])
def home():
    db = get_db()
    today_date = datetime.datetime.now().strftime('%Y-%m-%d')
    if request.method == "POST":
        date = request.form['date']
        db_date = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y%m%d')
        
        db.execute('INSERT INTO log_date (entry_date) values (?)', [db_date])
        db.commit()
        
    cur = db.execute('SELECT entry_date FROM log_date ORDER BY entry_date DESC')
    results = cur.fetchall()
    pretty_results = []
    db_results = []
    
    for dates in results:
        single_date = {}
        pretty_date = datetime.datetime.strptime(str(dates['entry_date']), '%Y%m%d').strftime('%B %d, %Y')
        single_date['entry_date'] =  pretty_date
        pretty_results.append(single_date)
        db_results.append(dates['entry_date'])
        
    cals, carbs, fat, protein = 0,0,0,0
    all_dates = db.execute('SELECT id FROM log_date')
    dates_foods_dict = {}
    for date in all_dates:
        total_foods = db.execute('SELECT * FROM food_date WHERE log_date_id = ?', [date['id']]).fetchall()
        food_ids = [i['food_id'] for i in total_foods]
        dates_foods_dict[date['id']] = food_ids

    
    final_list = []
    for i in list(dates_foods_dict.values()):
        cals, carbs, protein, fat = 0,0,0,0
        vals_dict = {}
        for k in i:
            for j in db.execute('SELECT * FROM food WHERE id=?', [k]):
                cals += j['calories']
                carbs += j['carbohydrates']
                protein += j['protein']
                fat += j['fat']
        vals_dict['cals'] = cals
        vals_dict['carbs'] = carbs
        vals_dict['protein'] = protein
        vals_dict['fat'] = fat
        final_list.append(vals_dict)


        
    return render_template('home.html', today_date=today_date,\
        results=db_results, e=enumerate(pretty_results), nutritional_vals=final_list)


@main_bp.route('/about')
def about():
    return render_template('about.html')