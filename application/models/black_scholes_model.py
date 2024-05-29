def black_scholes_currency(S, K, T, r_d, sigma, option_type='call'):
    from scipy.stats import norm
    import numpy as np

    # S = current exchange rate
    # K = strike price
    # T = time to maturity (in years)
    # r_d = domestic risk-free rate
    # sigma = volatility
    # option_type = 'call' or 'put'

    d1 = (np.log(S / K) + (r_d + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r_d * T) * norm.cdf(d2)
    else:  # put
        price = K * np.exp(-r_d * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    delta = norm.cdf(d1) if option_type == 'call' else -norm.cdf(-d1)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    theta = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) - r_d * K * np.exp(-r_d * T) * norm.cdf(d2 if option_type == 'call' else -d2)
    vega = S * norm.pdf(d1) * np.sqrt(T)
    rho_d = K * T * np.exp(-r_d * T) * norm.cdf(d2 if option_type == 'call' else -d2)

    return price, delta, gamma, theta, vega, rho_d
