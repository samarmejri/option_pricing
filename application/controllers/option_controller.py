from datetime import datetime
import numpy as np
import yfinance as yf
import logging 
from application.models.black_scholes_model import garman_kohlhagen
logging.basicConfig (
    filename="logfile.log" , filemode="w" , format="%(name)s - %(levelname)s - %(message)s" , level=logging.INFO
    
 )

def get_currency_pairs():
    currency_pairs = [
        'EURUSD=X', 'GBPUSD=X', 'USDJPY=X', 'AUDUSD=X', 'USDCAD=X', 
        'USDCHF=X', 'NZDUSD=X', 'EURGBP=X', 'EURJPY=X', 'GBPJPY=X', 
        'AUDJPY=X', 'AUDCAD=X', 'AUDCHF=X', 'AUDNZD=X', 'CADCHF=X',
        'EURAUD=X', 'EURCAD=X', 'EURCHF=X', 'EURNZD=X', 'GBPAUD=X', 
        'GBPCAD=X', 'GBPCHF=X', 'GBPNZD=X', 'NZDCAD=X', 'NZDCHF=X'
    ]
    return currency_pairs


def calculate_option_price(currency_pair , option_type, strike_prices, expiration_date, domestic_risk_free_rate, foreign_risk_free_rate):
    logging.info("paramter= %s %s %s %s %s %s " , currency_pair , option_type, strike_prices, expiration_date, domestic_risk_free_rate, foreign_risk_free_rate )
    exchange_rate_data = yf.Ticker(currency_pair)


    current_exchange_rate = exchange_rate_data.history(period='1d')['Close'][0]

    logging.info("current_exchange_rate %s" , current_exchange_rate )
    
    historical_data = exchange_rate_data.history(period='1y')

    returns = historical_data['Close'].pct_change().dropna()
    logging.info("returns %s",returns )
    volatility = returns.std() * np.sqrt(252)  # Annualized volatility
    logging.info("volatility %s",volatility )
    expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d')
    current_date = datetime.now()
    time_to_maturity = (expiration_date - current_date).days / 365.0  # in years

    results = {}
    logging.info("expiration_date %s",expiration_date )
    logging.info("current_date %s",current_date )
    logging.info("time_to_maturity  %s",time_to_maturity  )
     

    for strike_price in strike_prices:
        price, delta, gamma, theta, vega, rho_d, rho_f = garman_kohlhagen(
            current_exchange_rate, strike_price, time_to_maturity, 
            domestic_risk_free_rate, foreign_risk_free_rate, volatility, 
            option_type=option_type
        )

        logging.info("price %s %s %s %s %s %s %s ",price, delta, gamma, theta, vega, rho_d, rho_f  )
        
        results[strike_price] = {
            'option_price': price,
            'delta': delta,
            'gamma': gamma,
            'theta': theta,
            'vega': vega,
            'rho_d': rho_d,
            'rho_f': rho_f
        }

        logging.info("results %s  ", results )


    return results
