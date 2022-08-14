from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from cointracker.main.utils import draw_sparkline
import datetime
from cointracker import db
from cointracker.models import Sparkline
from cointracker.utils import get_cmc, get_eth_gas, get_gecko, get_global_metrics
from numerize import numerize

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
@main_bp.route('/home')
def home():


    coins = get_gecko(
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h%2C24h%2C7d%2C30d")

    necessary_pairs = ["market_cap_rank", "current_price",
                       "name", "image", "symbol", "price_change_percentage_24h", "market_cap", "total_volume",
                       "ath", "sparkline_in_7d", "price_change_percentage_1h_in_currency", "price_change_percentage_7d_in_currency",
                       "price_change_percentage_30d_in_currency"
                       ]

    coins = [{k: v for k, v in coin.items() if k in necessary_pairs}
             for coin in coins]

    for coin in coins:
        coin['athcondition'] = True if coin['ath'] < coin['current_price'] else False
        if coin['athcondition']:
            coin['percent_ath'] = f"{(coin['current_price'] / coin['ath'] - 1)*100:.2f}"
        else:
            coin['percent_ath'] = f"{(1 - coin['current_price'] / coin['ath'])*100:.2f}"
        coin['market_cap'] = numerize.numerize(float(coin['market_cap']))
        coin['total_volume'] = numerize.numerize(float(coin['total_volume']))
        coin['symbol'] = coin['symbol'].upper()
        coin['current_price'] = f"{coin['current_price']:,.2f}" if coin[
            'current_price'] > 0.001 else f"{coin['current_price']:,.5f}"
        coin['ath'] = f"{coin['ath']:,}"
        coin['price_change_percentage_24h'] = f"{coin['price_change_percentage_24h']:.2f}"
        coin['price_change_percentage_1h_in_currency'] = f"{coin['price_change_percentage_1h_in_currency']:.2f}"
        coin['price_change_percentage_7d_in_currency'] = f"{coin['price_change_percentage_7d_in_currency']:.2f}"
        coin['price_change_percentage_30d_in_currency'] = f"{coin['price_change_percentage_30d_in_currency']:.2f}"

    sparkline_values = [i['sparkline_in_7d']['price'] for i in coins]
    q = Sparkline.query.all()
    if not q:
        draw_sparkline(sparkline_values)
        q = Sparkline(date_updated=datetime.datetime.now().date())
        db.session.add(q)
        db.session.commit()
    else:
        if q[0].date_updated != datetime.datetime.now().date():
            draw_sparkline(sparkline_values)
            q[0].date_updated = datetime.datetime.now().date()
            db.session.commit()

    return render_template('home.html', global_metrics=get_global_metrics(), coins=coins, sparkline_values=sparkline_values)


@ main_bp.route('/about')
def about():
    pass
