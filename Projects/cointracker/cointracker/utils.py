from requests import Session, get
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os


def get_json(url, params=None):
    with Session() as session:
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': os.environ.get('COINMARKETCAP_API_KEY', None),
        }
        try:
            response = session.get(url, params=params, headers=headers)
            return json.loads(response.text)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
            return None


def get_eth_gas(url="https://api.blocknative.com/gasprices/blockprices"):
    headers = {
        "Authorization": os.environ.get("ETHGAS_API", None)
    }
    try:
        response = get(url, headers=headers)
        return response.json()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return None


def get_gecko(url):
    try:
        response = get(url)
        return response.json()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return None
