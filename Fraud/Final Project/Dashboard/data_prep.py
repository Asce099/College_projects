import os
import pandas as pd

# Load the static data
static_data = pd.read_csv('data/fundamental_final.csv')

# Load and process the YoY data
financial_data = {}
financial_data_files = [
    'data/financials/current_assets.csv', 'data/financials/current_liabilities.csv', 'data/financials/long_term_borrowings.csv',
    'data/financials/sales.csv', 'data/financials/total_assets.csv', 'data/financials/total_expenses.csv',
    'data/financials/total_income.csv', 'data/financials/turnover.csv', 'data/financials/yield.csv'
]

for file in financial_data_files:
    key = os.path.basename(file).split('.')[0]  # Use the file name as the key
    df = pd.read_csv(file)
    
    # Merge static and YoY data on the 'name' column
    df = pd.merge(static_data, df, on='name', how='inner')
    
    financial_data[key] = df

# Save processed data to a common format (e.g., CSV or Pickle) for easy access in the Streamlit app
for key, df in financial_data.items():
    df.to_csv(f'data/prep_data/{key}_data.csv', index=False)
