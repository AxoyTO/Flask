from weather_app import gc, db
from weather_app.models import City
import json


def is_valid_city(city):
    city = gc.get_cities_by_name(city)
    if city:
        return True
    else:
        return False


def get_country_code(city):
    city = gc.get_cities_by_name(city)
    return list(city[0].values())[0]['countrycode']


def get_all_cities():
    city = gc.get_cities()
    all_cities = [i['name'] for i in city.values()]
    return all_cities


def add_city(city, r):
    city = City(name=city.upper(),
                lat=r['latitude'],
                lon=r['longitude'],
                tz=r['timezone'],
                date=r['days'][0]['datetime'],
                countrycode=get_country_code(city.title()),
                tempmax=r['days'][0]['tempmax'],
                tempmin=r['days'][0]['tempmin'],
                temperature=r['currentConditions']['temp'],
                feelslike=r['currentConditions']['feelslike'],
                humidity=r['currentConditions']['humidity'],
                pressure=r['currentConditions']['pressure'],
                sunrise=r['days'][0]['sunrise'],
                sunset=r['days'][0]['sunset'],
                lastcheck=r['currentConditions']['datetime'],
                description=r['days'][0]['description'],
                icon=r['days'][0]['icon']
                )
    db.session.add(city)
    db.session.commit()


def update_city(city, r):
    city.date = r['days'][0]['datetime']
    city.tempmax = r['days'][0]['tempmax']
    city.tempmin = r['days'][0]['tempmin']
    city.temperature = r['currentConditions']['temp']
    city.feelslike = r['currentConditions']['feelslike']
    city.humidity = r['currentConditions']['humidity']
    city.pressure = r['currentConditions']['pressure']
    city.lastcheck = r['currentConditions']['datetime']
    city.description = r['days'][0]['description']
    city.icon = r['days'][0]['icon']
    db.session.commit()
