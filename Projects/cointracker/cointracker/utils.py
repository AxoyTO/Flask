from requests import Session, get
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from numerize import numerize
import os


def get_cmc(url, params=None):
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


def get_global_metrics():
    global_metrics = get_cmc(
        'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest')

    total_coins = global_metrics['data']['active_cryptocurrencies']
    total_exchanges = global_metrics['data']['active_exchanges']
    total_mcap = numerize.numerize(float(
        global_metrics['data']['quote']['USD']['total_market_cap']))
    total_24h_vol = numerize.numerize(float(
        global_metrics['data']['quote']['USD']['total_volume_24h']))
    btc_dom = f"{global_metrics['data']['btc_dominance']:.1f}"
    eth_dom = f"{global_metrics['data']['eth_dominance']:.1f}"
    eth_gas = int(get_eth_gas()['blockPrices'][0]['baseFeePerGas'])

    global_metrics = [total_coins, total_exchanges,
                      total_mcap, total_24h_vol, btc_dom, eth_dom, eth_gas]
    return global_metrics
