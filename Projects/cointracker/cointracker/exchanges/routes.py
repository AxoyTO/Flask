from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from numerize import numerize
from ..utils import get_gecko, get_global_metrics

exchanges_bp = Blueprint('exchanges', __name__)


@exchanges_bp.route('/exchanges')
def exchanges():
    exchanges = get_gecko("https://api.coingecko.com/api/v3/exchanges?page=1")
    necessary_pairs = ["trust_score_rank", "trust_score",
                       "year_established", "name", "trade_volume_24h_btc", "image", "url", "country"]

    currency = 'usd'

    btc_price = get_gecko(
        f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies={currency}")['bitcoin'][currency]

    exchanges = [{k: v for k, v in exchange.items() if k in necessary_pairs}
                 for exchange in exchanges]

    for exchange in exchanges:
        exchange['trade_volume_24h'] = numerize.numerize(
            exchange['trade_volume_24h_btc'] * btc_price)
        exchange['url'] = "https://www.kraken.com/" if exchange['name'] == 'Kraken' else exchange['url']
        exchange['year_established'] = '2013' if exchange['name'] == 'Gate.io' else exchange['year_established']
        exchange['year_established'] = "—" if not exchange['year_established'] else exchange['year_established']

    return render_template('exchanges.html', global_metrics=get_global_metrics(), exchanges=exchanges)
