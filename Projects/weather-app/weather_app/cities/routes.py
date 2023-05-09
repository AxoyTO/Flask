from flask import Blueprint, render_template, url_for, redirect, flash
from werkzeug.exceptions import HTTPException
import requests
import json
from weather_app import API_KEY, db
from weather_app.cities.utils import get_all_cities, add_city, update_city, is_valid_city
from weather_app.models import City
from weather_app.cities.forms import CityForm

cities_bp = Blueprint('cities', __name__)
weather_data = []


@cities_bp.route('/', methods=['GET', 'POST'])
@cities_bp.route('/home', methods=['GET', 'POST'])
def home():
    cities = City.query.all()
    city_form = CityForm()

    if city_form.validate_on_submit():
        city = city_form.city.data.upper()

        if not is_valid_city(city.title()):
            flash(f"Can't find city: {city}", 'error')
            return redirect(url_for('cities.home'))
        
        db_city = City.query.filter_by(name=city).first()

        if db_city is None:
            URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&include=days%2Ccurrent%2Cevents%2Calerts&key={API_KEY}&contentType=json"
            try:
                response = requests.get(URL)
                print(response)
                if response.status_code != 200:
                    raise HTTPException(response.status_code)
            except HTTPException as e:
                return e

            r = response.json()

            add_city(city, r)
            return redirect(url_for('cities.home'))
        else:
            flash(f"{city} City already exists", 'warning')
            return redirect(url_for('cities.home'))

    return render_template('home.html', all_cities=json.dumps(get_all_cities()), cities=cities, form=city_form)


@cities_bp.route('/home/reload', methods=['GET'])
def reload_all():
    cities = City.query.all()
    for city in cities:
        URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city.name}?unitGroup=metric&include=days%2Ccurrent%2Cevents%2Calerts&key={API_KEY}&contentType=json"
        try:
            response = requests.get(URL)
            if response.status_code != 200:
                raise HTTPException(response.status_code)
        except HTTPException as e:
            return e

        r = response.json()
        update_city(city, r)
    return redirect(url_for('cities.home'))


@cities_bp.route('/home/reload/<int:id>', methods=['GET'])
def reload(id):
    city = City.query.filter_by(id=id).first()
    URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city.name}?unitGroup=metric&include=days%2Ccurrent%2Cevents%2Calerts&key={API_KEY}&contentType=json"
    print(city)
    try:
        response = requests.get(URL)
        if response.status_code != 200:
            raise HTTPException(response.status_code)
    except HTTPException as e:
        return e

    r = response.json()
    update_city(city, r)
    return redirect(url_for('cities.home'))


@cities_bp.route('/delete', methods=['GET'])
def delete_all():
    db.engine.execute('DELETE FROM city')
    return redirect(url_for('cities.home'))


@cities_bp.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    city = City.query.filter_by(id=id).first()
    db.session.delete(city)
    db.session.commit()
    return redirect(url_for('cities.home'))
