"""
Script Name: Data Cleaning
Description: Loads the Nintendo Switch dataset, handles missing data, 
and saves a cleaned version if needed.
"""

import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    
    df.drop_duplicates(inplace=True)
    df.sort_values(by='Date', inplace=True)
    
    df.fillna(method='ffill', inplace=True)
    
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_file = 'data/dataset1.csv'
    output_file = 'data/dataset1_cleaned.csv'
    clean_data(input_file, output_file)
    print("Data cleaning complete. Cleaned file saved to:", output_file)
