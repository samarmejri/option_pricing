from flask import Blueprint, render_template, request
from application.controllers.option_controller import calculate_option_price, get_currency_pairs

option_routes = Blueprint('option_routes', __name__)

@option_routes.route('/')
def index():
    currency_pairs = get_currency_pairs()
    return render_template('option_form.html', currency_pairs=currency_pairs)

@option_routes.route('/calculate', methods=['POST'])
def calculate():
    currency_pair = request.form['currency_pair']
    option_type = request.form['option_type']
    strike_prices = [float(price.strip()) for price in request.form['strike_prices'].split(',')]
    expiration_date = request.form['expiration_date']
    domestic_risk_free_rate = float(request.form['domestic_risk_free_rate'])
    foreign_risk_free_rate = float(request.form['foreign_risk_free_rate'])  # New input

    results = calculate_option_price(currency_pair, option_type, strike_prices, expiration_date, domestic_risk_free_rate, foreign_risk_free_rate)
    
    return render_template('option_result.html', results=results)
