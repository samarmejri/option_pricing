# garman_kohlhagen_model.py
from scipy.stats import norm
import numpy as np
import logging 

logging.basicConfig (
    filename="logfile.log" , filemode="w" , format="%(name)s - %(levelname)s - %(message)s" , level=logging.INFO
    
 )

def garman_kohlhagen(S, K, T, r_d, r_f, sigma, option_type='put'):
    logging.info("paramter= %s %s %s %s %s %s %s " ,S, K, T, r_d, r_f, sigma, option_type)
    



    d1 = (np.log(S / K) + (r_d - r_f + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    logging.info("d1 d2= %s %s  " ,d1, d2 )


    if option_type == 'put':
      #  price = S * np.exp(-r_f * T) * norm.cdf(d1)  - K * np.exp(-r_d * T) * norm.cdf(d2)
      #  logging.info(" call price=%s  " ,price ) 
      price = K * np.exp(-r_d * T) * norm.cdf(-d2) - S * np.exp(-r_f * T) * norm.cdf(-d1)
      logging.info("put price=%s  " ,price )
        
    else:  # put
       # price = K * np.exp(-r_d * T) * norm.cdf(-d2) - S * np.exp(-r_f * T) * norm.cdf(-d1)
       # logging.info("put price=%s  " ,price )  

        price = S * np.exp(-r_f * T) * norm.cdf(d1)  - K * np.exp(-r_d * T) * norm.cdf(d2)
        logging.info(" call price=%s  " ,price ) 

    delta = np.exp(-r_f * T) * norm.cdf(d1) if option_type == 'call' else -np.exp(-r_f * T) * norm.cdf(-d1)
    gamma = np.exp(-r_f * T) * norm.pdf(d1) / (S * sigma * np.sqrt(T))
    theta = -(S * np.exp(-r_f * T) * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) - r_d * K * np.exp(-r_d * T) * norm.cdf(d2 if option_type == 'call' else -d2)
    vega = S * np.exp(-r_f * T) * norm.pdf(d1) * np.sqrt(T)
    rho_d = K * T * np.exp(-r_d * T) * norm.cdf(d2 if option_type == 'call' else -d2)
    rho_f = -S * T * np.exp(-r_f * T) * norm.cdf(d1 if option_type == 'call' else -d1)

    return price, delta, gamma, theta, vega, rho_d, rho_f
