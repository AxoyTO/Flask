from flask import render_template, Blueprint

main_bp = Blueprint('main', __name__)


@main_bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
