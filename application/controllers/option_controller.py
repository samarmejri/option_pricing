from datetime import datetime
import numpy as np
import yfinance as yf
from application.models.black_scholes_model import black_scholes_currency

def get_currency_pairs():
    # Common currency pairs
    currency_pairs = [
        'EURUSD=X', 'GBPUSD=X', 'USDJPY=X', 'AUDUSD=X', 'USDCAD=X', 
        'USDCHF=X', 'NZDUSD=X', 'EURGBP=X', 'EURJPY=X', 'GBPJPY=X', 
        'AUDJPY=X', 'AUDCAD=X', 'AUDCHF=X', 'AUDNZD=X', 'CADCHF=X',
        'EURAUD=X', 'EURCAD=X', 'EURCHF=X', 'EURNZD=X', 'GBPAUD=X', 
        'GBPCAD=X', 'GBPCHF=X', 'GBPNZD=X', 'NZDCAD=X', 'NZDCHF=X'
    ]
    return currency_pairs

def calculate_option_price(currency_pair, option_type, strike_prices, expiration_date, domestic_risk_free_rate):
    exchange_rate_data = yf.Ticker(currency_pair)
    current_exchange_rate = exchange_rate_data.history(period='1d')['Close'][0]

    historical_data = exchange_rate_data.history(period='1y')
    returns = historical_data['Close'].pct_change().dropna()
    volatility = returns.std() * np.sqrt(252)  # Annualized volatility

    expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d')
    current_date = datetime.now()
    time_to_maturity = (expiration_date - current_date).days / 365.0  # in years

    results = {}

    for strike_price in strike_prices:
        price, delta, gamma, theta, vega, rho_d = black_scholes_currency(
            current_exchange_rate, strike_price, time_to_maturity, 
            domestic_risk_free_rate, volatility, 
            option_type=option_type
        )
        
        results[strike_price] = {
            'option_price': price,
            'delta': delta,
            'gamma': gamma,
            'theta': theta,
            'vega': vega,
            'rho_d': rho_d
        }

    return results
