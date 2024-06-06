# garman_kohlhagen_model.py

def garman_kohlhagen(S, K, T, r_d, r_f, sigma, option_type='call'):
    from scipy.stats import norm
    import numpy as np

    d1 = (np.log(S / K) + (r_d - r_f + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        price = S * np.exp(-r_f * T) * norm.cdf(d1) - K * np.exp(-r_d * T) * norm.cdf(d2)
    else:  # put
        price = K * np.exp(-r_d * T) * norm.cdf(-d2) - S * np.exp(-r_f * T) * norm.cdf(-d1)

    delta = np.exp(-r_f * T) * norm.cdf(d1) if option_type == 'call' else -np.exp(-r_f * T) * norm.cdf(-d1)
    gamma = np.exp(-r_f * T) * norm.pdf(d1) / (S * sigma * np.sqrt(T))
    theta = -(S * np.exp(-r_f * T) * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) - r_d * K * np.exp(-r_d * T) * norm.cdf(d2 if option_type == 'call' else -d2)
    vega = S * np.exp(-r_f * T) * norm.pdf(d1) * np.sqrt(T)
    rho_d = K * T * np.exp(-r_d * T) * norm.cdf(d2 if option_type == 'call' else -d2)
    rho_f = -S * T * np.exp(-r_f * T) * norm.cdf(d1 if option_type == 'call' else -d1)

    return price, delta, gamma, theta, vega, rho_d, rho_f
