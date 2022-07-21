from webbrowser import get
from flask import flash, render_template, redirect, request, url_for, Blueprint
from foodtracker.db import get_db

foods_bp = Blueprint('foods', __name__) 

@foods_bp.route('/add_food', methods=['GET', 'POST'])
def food():
    db = get_db()
    
    if request.method == 'POST':
        name = request.form['foodname']
        protein = int(request.form['protein'])
        carbs = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])
        
        calories = protein * 4 + carbs * 4 + fat * 9
        print(protein, carbs, fat, 4*protein+ 4*carbs+9*fat, calories)
        
        db.execute('INSERT INTO food (name, protein, carbohydrates, fat, calories) values (?, ?, ?, ?, ?)',
                   [name, protein, carbs, fat, calories])
        db.commit()
        flash('{} added successfully!'.format(request.form['foodname']), 'success')
        
    cur = db.execute('SELECT id, name, protein, carbohydrates, fat, calories FROM food')
    results = cur.fetchall()
    return render_template('food.html', results=results)


@foods_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):    
    db = get_db()
    cur = db.execute('SELECT id, name, protein, carbohydrates, fat, calories FROM food')
    results = cur.fetchall()
    food = db.execute('SELECT id, name, protein, carbohydrates, fat, calories FROM food WHERE id = ?', [id]).fetchone()

    if request.method == "POST":
        name = request.form['foodname']
        protein = int(request.form['protein'])
        carbs = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])        
        calories = protein * 4 + carbs * 4 + fat * 9
        
        db.execute('UPDATE food SET name = ?, protein = ?, carbohydrates = ?, fat = ?, calories = ? WHERE id = ?',
                   [name,protein,carbs,fat,calories,id])
        db.commit()
        return redirect(url_for('foods.food'))
        
    return render_template('food.html', results=results, food_upd=food)


@foods_bp.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    db = get_db()
    food = db.execute('SELECT name FROM food WHERE id = ?', [id]).fetchone()
    db.execute('DELETE FROM food WHERE id = ?', [id])
    db.commit()
    try:
        flash('{} deleted successfully'.format(food['name']), 'success')
    except:
        flash('Error deleting. Such food does not exist in the database!', 'danger')
    return redirect(url_for('foods.food'))