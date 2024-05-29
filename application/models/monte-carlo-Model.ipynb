{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "86d9bb0d-6988-4f49-90de-c679bb8fef21",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import scipy.stats as stats\n",
    "import matplotlib.pyplot as plt\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e872c788-cebf-4378-97a8-64ea48e572ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Option parameters\n",
    "S0 = 100     # Initial stock price\n",
    "K = 100      # Strike price\n",
    "T = 1        # Time to maturity (in years)\n",
    "r = 0.05     # Risk-free rate\n",
    "sigma = 0.2  # Volatility\n",
    "\n",
    "# Simulation parameters\n",
    "n_simulations = 10000\n",
    "n_steps = 100\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0edde42d-5776-4a91-9751-eba84d5ba058",
   "metadata": {},
   "outputs": [],
   "source": [
    "def monte_carlo_option_pricing(S0, K, T, r, sigma, n_simulations, n_steps):\n",
    "    dt = T / n_steps\n",
    "    discount_factor = np.exp(-r * T)\n",
    "    \n",
    "    # Simulate paths\n",
    "    S = np.zeros((n_steps + 1, n_simulations))\n",
    "    S[0] = S0\n",
    "    for t in range(1, n_steps + 1):\n",
    "        Z = np.random.standard_normal(n_simulations)\n",
    "        S[t] = S[t-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)\n",
    "    \n",
    "    # Calculate the payoff for a European call option\n",
    "    payoff = np.maximum(S[-1] - K, 0)\n",
    "    \n",
    "    # Discount the payoff back to present value\n",
    "    option_price = np.mean(payoff) * discount_factor\n",
    "    return option_price\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "30ccb74e-10b5-4826-b96b-c625d3ed483a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The estimated option price is: 10.20\n"
     ]
    }
   ],
   "source": [
    "option_price = monte_carlo_option_pricing(S0, K, T, r, sigma, n_simulations, n_steps)\n",
    "print(f\"The estimated option price is: {option_price:.2f}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8752b172-579e-4600-b42c-4e19ed57fa85",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
