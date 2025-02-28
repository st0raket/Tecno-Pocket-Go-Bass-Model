import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from helper_functions import bass_cumulative

def main():
    switch_df = pd.read_csv('data/dataset1.csv')
    
    switch_df['Date'] = pd.to_datetime(switch_df['Date'], format='%Y-%m')
    switch_df.sort_values('Date', inplace=True)
    
    # Extracting the last entry for each year
    switch_df['Year'] = switch_df['Date'].dt.year
    yearly_df = switch_df.groupby('Year').tail(1).copy()
    # This ensures we get the final cumulative sales figure for each year
    
    yearly_data_path = 'data/nintendo_switch_sales_yearly.csv'
    yearly_df.to_csv(yearly_data_path, index=False)
    print(f"Saved yearly Switch data to: {yearly_data_path}")
    
    yearly_df.sort_values('Year', inplace=True)
    yearly_df.reset_index(drop=True, inplace=True)
    yearly_df['t'] = yearly_df.index + 1
    
    yearly_df.rename(columns={'Cumulative_Sales_millions': 'S'}, inplace=True)
    
    t_vals = yearly_df['t'].values
    S_vals = yearly_df['S'].values
    
    print("\n=== Annual Nintendo Switch Data (Last Entry per Year) ===")
    print(yearly_df[['Year', 'Date', 't', 'S']])
    
    p0 = [0.03, 0.4, 150]  
    params, _ = curve_fit(bass_cumulative, t_vals, S_vals, p0=p0, maxfev=10000)
    p_est, q_est, M_est = params
    
    print("\n===== Bass Model Parameters (Annual Data) =====")
    print(f"Estimated p = {p_est:.4f}")
    print(f"Estimated q = {q_est:.4f}")
    print(f"Estimated M = {M_est:.2f} million")
    
    S_fit = bass_cumulative(t_vals, p_est, q_est, M_est)
    plt.figure(figsize=(8,5))
    plt.scatter(t_vals, S_vals, label='Actual Annual Data', alpha=0.7)
    plt.plot(t_vals, S_fit, 'r-', label='Bass Fit')
    plt.xlabel('Time (Annual Index)')
    plt.ylabel('Cumulative Sales (millions)')
    plt.title('Nintendo Switch (Annual) Bass Diffusion Fit')
    plt.legend()
    plt.savefig('img/switch_bass_fit_annual.png')
    plt.close()
    
    future_start = yearly_df['t'].max() + 1
    future_end = future_start + 8  
    future_t = np.arange(future_start, future_end)
    
    new_product_pred = bass_cumulative(future_t, p_est, q_est, M_est)
    
    forecast_df = pd.DataFrame({
        't': future_t,
        'Cumulative_Adoption': new_product_pred
    })
    
    forecast_path = 'data/product_forecast.csv'
    forecast_df.to_csv(forecast_path, index=False)
    print(f"\n===== Forecast for New Innovation (No Parameter Adjustment) =====")
    print(forecast_df)
    print(f"Saved forecast to: {forecast_path}\n")
    
    # Plot the forecast graph and save it in the img folder
    plt.figure(figsize=(8,5))
    plt.plot(forecast_df['t'], forecast_df['Cumulative_Adoption'], 'bo-', label='Forecast')
    plt.xlabel('Time (Annual Index)')
    plt.ylabel('Cumulative Adoption (millions)')
    plt.title('Forecast for Tecno Pocket Go Diffusion')
    plt.legend()
    forecast_graph_path = 'img/product_forecast.png'
    plt.savefig(forecast_graph_path)
    plt.close()
    print(f"Saved forecast graph to: {forecast_graph_path}\n")

if __name__ == '__main__':
    main()
