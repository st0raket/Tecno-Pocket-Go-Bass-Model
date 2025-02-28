# script2.py
"""
Script Name: Bass Model Estimation & Forecast
Description:
    1) Reads the cleaned Nintendo Switch data (look-alike innovation).
    2) Estimates Bass Model parameters p, q, M from that data.
    3) Uses the exact same p, q, M to forecast the new product's (e.g. Tecno Pocket Go) adoption.
       (No parameter adjustments are made.)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from helper_functions import bass_cumulative, create_time_index

def main():
    # 1) Load the cleaned dataset for the historical analog (Nintendo Switch)
    df = pd.read_csv('data/dataset1_cleaned.csv')
    
    # 2) Create a time index for each observation (1, 2, 3, ...)
    df = create_time_index(df)
    t_vals = df['t'].values
    S_vals = df['Cumulative_Sales_millions'].values
    
    # 3) Estimate Bass Model Parameters from the historical data
    #    (p, q, M) using the continuous Bass cumulative form
    p0 = [0.03, 0.4, 150]  # Initial guesses for p, q, M
    params, _ = curve_fit(bass_cumulative, t_vals, S_vals, p0=p0, maxfev=10000)
    p_est, q_est, M_est = params
    
    print("===== Fitted Bass Parameters (Nintendo Switch) =====")
    print(f"Estimated p = {p_est:.4f}")
    print(f"Estimated q = {q_est:.4f}")
    print(f"Estimated M = {M_est:.2f} million")
    
    # 4) Plot the Bass fit vs. actual data
    S_pred = bass_cumulative(t_vals, p_est, q_est, M_est)
    
    plt.figure(figsize=(8,5))
    plt.scatter(t_vals, S_vals, label='Actual Data', alpha=0.7)
    plt.plot(t_vals, S_pred, 'r-', label='Bass Fit')
    plt.xlabel('Time Index (t)')
    plt.ylabel('Cumulative Sales (millions)')
    plt.title('Nintendo Switch Bass Diffusion Fit')
    plt.legend()
    plt.savefig('img/switch_bass_fit.png')
    plt.close()
    
    # 5) Forecast the New Product (e.g., Tecno Pocket Go) Using the SAME p, q, M
    #    NO parameter adjustments are made here.
    #    We'll forecast 8 future periods (t=1..8). In reality, you'd decide how
    #    to map these "periods" to months/years.
    
    forecast_t = np.arange(1, 9, 1)
    new_product_pred = bass_cumulative(forecast_t, p_est, q_est, M_est)
    
    # Create a DataFrame for the forecast
    forecast_df = pd.DataFrame({
        't': forecast_t,
        'Cumulative_Adoption': new_product_pred
    })
    
    # Save to CSV
    forecast_df.to_csv('data/product_forecast.csv', index=False)
    
    print("\n===== Forecast for the New Innovation (Using SAME p, q, M) =====")
    print(forecast_df)

if __name__ == '__main__':
    main()
