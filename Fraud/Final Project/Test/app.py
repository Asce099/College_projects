import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import os

# Import the create_gauge_chart function from gauge_chart.py
from plots import gauge_chart
from plots import area_chart

# Create a dictionary to store financial data
financial_data = {}

# Define the years for which you have data columns
years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']

# Define the fundamental columns you want to extract
fundamental_columns = [
    'ticker', 'industry', 'NIFTY closing', 'Date', 'Market Capitalisation',
    'EPS', 'P/E', 'P/B', 'Beta', 'Industry PE', 'Industry PB', 'Risk_Score', 'risk'
]

# List of financial data files
financial_data_files = [
    'data/prep_data/current_assets_data.csv',
    'data/prep_data/current_liabilities_data.csv',
    'data/prep_data/long_term_borrowings_data.csv',
    'data/prep_data/sales_data.csv',
    'data/prep_data/total_assets_data.csv',
    'data/prep_data/total_expenses_data.csv',
    'data/prep_data/total_income_data.csv',
    'data/prep_data/turnover_data.csv',
    'data/prep_data/yield_data.csv'
]

for file in financial_data_files:
    key = os.path.basename(file).split('_data.csv')[0]  # Use the file name as the key
    df = pd.read_csv(file)
    
    # Create a dictionary to store the financial data for each company
    financial_data[key] = {}
    
    # Iterate over rows and store data by company
    for _, row in df.iterrows():
        company_name = row['name']
        financial_data[key][company_name] = {}
        
        # Store year-wise data
        for year in years:
            year_str = str(year)
            if year_str in row:
                financial_data[key][company_name][year_str] = row[year_str]
            else:
                financial_data[key][company_name][year_str] = None  # Handle missing data
            
        # Store fundamental financial values
        for column in fundamental_columns:
            if column in row:
                financial_data[key][company_name][column] = row[column]
            else:
                financial_data[key][company_name][column] = None  # Handle missing data

# Sidebar for selecting the company
selected_company = st.sidebar.selectbox("Select Company", list(financial_data['current_assets'].keys()))

# Define a mapping between risk ratings and numeric values
risk_mapping = {
    'Highly risky': 1,
    'Moderately risky': 2,
    'Non risky': 3,
    'Investment Worthy': 4
}

# Function to get risk rating for the selected company
def get_risk_rating(selected_company):
    # Retrieve the risk rating for the selected company from the financial_data dictionary
    # Replace 'YourRiskRatingColumnName' with the actual column name for risk ratings
    try:
        risk_rating = financial_data['current_assets'][selected_company]['risk']
        return risk_mapping.get(risk_rating, 2)  # Use 2 (Non risky) as the default value if the rating is not found
    except KeyError:
        return 2  # Default to Non risky if data is not available

# Get risk rating for the selected company
selected_company_risk = get_risk_rating(selected_company)

# Create a gauge chart using Plotly by calling the function from gauge_chart.py
st.subheader("Risk Score")
gauge_chart.create_gauge_chart(selected_company, selected_company_risk)


#Area Chart
# Define the financial metrics columns you want to plot
financial_metrics_columns = ['Yield', 'Turnover']

# Create a DataFrame for the selected company's data
selected_company_data = pd.DataFrame({
    'Year': years,
    'Yield': [financial_data['yield'][selected_company][year] for year in years],
    'Turnover': [financial_data['turnover'][selected_company][year] for year in years]
})

st.subheader("Area Chart")
area_chart.create_area_chart(selected_company, selected_company_data, financial_metrics_columns, years)
# Include code for your area chart here, or import it as well

st.subheader("Sales and Income Plot")
# Include code for your sales and income plot here, or import it as well

st.subheader("P/E Comparison")
# Include code for your P/E comparison here, or import it as well

st.subheader("P/B Comparison")
# Include code for your P/B comparison here, or import it as well