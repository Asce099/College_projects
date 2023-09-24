#app.py
from asyncio import streams
import streamlit as st
import plotly.express as px
import pandas as pd
import os
import plotly.graph_objects as go
import numpy as np

# The rest of your Streamlit app goes here
# Add your financial dashboard components below this line
st.title("Financial Health Dashboard - Indian Equity Market")

# Create a dictionary to store financial data
financial_data = {}

# Define the years for which you have data columns
years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']

# Define the fundamental columns you want to extract
fundamental_columns = [
    'ticker', 'industry', 'NIFTY closing', 'Date', 'Market Capitalisation',
    'EPS', 'P/E', 'P/B', 'Beta', 'Industry PE', 'Industry PB', 'Risk_Score', 'risk'
]
# Get the current directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the directory where your data files are located
data_dir = os.path.join(script_dir, 'data', 'prep_data')

# List of financial data files with absolute paths
financial_data_files = [
    os.path.join(data_dir, 'current_assets_data.csv'),
    os.path.join(data_dir, 'current_liabilities_data.csv'),
    os.path.join(data_dir, 'long_term_borrowings_data.csv'),
    os.path.join(data_dir, 'sales_data.csv'),
    os.path.join(data_dir, 'total_assets_data.csv'),
    os.path.join(data_dir, 'total_expenses_data.csv'),
    os.path.join(data_dir, 'total_income_data.csv'),
    os.path.join(data_dir, 'turnover_data.csv'),
    os.path.join(data_dir, 'yield_data.csv')
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
##################################################################################################################################################Company selected
# Extract the selected company's data
selected_company_data = financial_data['current_assets'][selected_company]
# Create a Streamlit sidebar to display selected company information

st.sidebar.markdown(f"**{selected_company} Information**")
st.sidebar.markdown(f"**Company Name:** {selected_company}")
st.sidebar.markdown(f"**Ticker:** {selected_company_data['ticker']}")
st.sidebar.markdown(f"**Beta:** {selected_company_data['Beta']}")
st.sidebar.markdown(f"**EPS:** {selected_company_data['EPS']}")
st.sidebar.markdown(f"**Market Cap:** {selected_company_data['Market Capitalisation']}")
st.sidebar.markdown(f"**Industry:** {selected_company_data['industry']}")

# Create KPI cards using Plotly with custom color and font
fig = go.Figure()

fig.add_trace(
    go.Indicator(
        mode="number",
        value=selected_company_data['Beta'],
        title="Beta",
        domain={'x': [0, 0.25], 'y': [0, 1]},
    )
)

fig.add_trace(
    go.Indicator(
        mode="number",
        value=selected_company_data['EPS'],
        title="EPS",
        domain={'x': [0.35, 0.6], 'y': [0, 1]},
    )
)

fig.add_trace(
    go.Indicator(
        mode="number",
        value=selected_company_data['Market Capitalisation'],
        title="Market Cap in Million ₹",
        domain={'x': [0.7, 1], 'y': [0, 1]},
    )
)

fig.update_layout(
    grid={'rows': 1, 'columns': 3, 'xgap': 0.1},  # Adjust the xgap value
)

st.plotly_chart(fig)
#########################################################################################################################################KPIs
# Define a mapping between risk ratings and numeric values
risk_mapping = {
    'Highly risky': 1,
    'Moderately risky': 2,
    'Non risky': 3,
    'Investment Worthy': 4
}

# Function to get risk rating for the selected company
def get_risk_rating(selected_company):
    try:
        risk_rating = financial_data['current_assets'][selected_company]['risk']
        return risk_mapping.get(risk_rating, 2) 
    except KeyError:
        return 2  # Default to Non risky if data is not available

# Get risk rating for the selected company
selected_company_risk = get_risk_rating(selected_company)

# Create a gauge chart using Plotly
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=selected_company_risk,
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': "Risk Rating"},
    gauge={
        'axis': {'range': [0, 4],  'tickwidth': 1, 'tickcolor': "black"},
        'bar': {'color': "black"},  # Set the numeric range
        'steps': [
            {'range': [0, 1], 'color': "#D60A2A"},
            {'range': [1, 2], 'color': "#F6C420"},
            {'range': [2, 3], 'color': "#59E34C"},
            {'range': [3, 4], 'color': "#4699E3"}  # Add the fourth color range for 'Investment Worthy'
        ],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.75,
            'value': selected_company_risk
        }
    }
))

# Define labels for the numeric values
risk_labels = {1: 'Highly risky', 2: 'Moderately risky', 3: 'Non risky', 4: 'Investment Worthy'}

st.header(f"Risk Rating: {risk_labels[selected_company_risk]}")
# Show the gauge chart
st.plotly_chart(fig)
######################################################################################################################################################Risk Meter
# Define the financial metrics columns you want to plot
financial_metrics_columns = ['Yield', 'Turnover']

# Create a DataFrame for the selected company's data
selected_company_data = pd.DataFrame({
    'Year': years,
    'Yield': [financial_data['yield'][selected_company][year] for year in years],
    'Turnover': [financial_data['turnover'][selected_company][year] for year in years]
})

# Create an area chart for Yield and Turnover
fig = px.area(
    selected_company_data,
    x='Year',
    y=financial_metrics_columns,
    title=f'{", ".join(financial_metrics_columns)} Over the Years for {selected_company}',
    labels={'Year': 'Year', 'value': 'Value'},
    width=800, height=400,  # Customize the chart size
    color_discrete_map={'Yield': '#4699E3', 'Turnover': '#46E36E'}  # Specify colors for each metric
)

# Customize the chart layout (optional)
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Value',
    legend_title='Metrics',
)

st.header(f"Yield Turnover Analysis")
# Show the area chart
st.plotly_chart(fig)
#################################################################################################################################################################################Yield, turnover Plotted

# Create a DataFrame for the selected company's data
selected_company_data = pd.DataFrame({
    'Year': years,
    'Sales (Million Rs)': [financial_data['sales'][selected_company][year] / 1e6 for year in years],
    'Total Income (Million Rs)': [financial_data['total_income'][selected_company][year] / 1e6 for year in years]  
})

# Calculate YoY total income
yoy_total_income = [0] + [(income - selected_company_data['Total Income (Million Rs)'][i - 1]) / selected_company_data['Total Income (Million Rs)'][i - 1] * 100
                           for i, income in enumerate(selected_company_data['Total Income (Million Rs)']) if i > 0]

# Determine colors based on YoY Total Income (%)
income_colors = ['#46E36E' if income >= 0 else '#E3464E' for income in yoy_total_income]

# Create a figure with dual axes
fig = go.Figure()

# Add a bar trace for YoY Total Income (%) with color mapping
fig.add_trace(go.Bar(x=selected_company_data['Year'][1:], y=yoy_total_income, name='YoY Total Income (%)', marker_color=income_colors))

# Add a line trace for Total Sales with the specified color
fig.add_trace(go.Scatter(x=selected_company_data['Year'], y=selected_company_data['Sales (Million Rs)'], name='Total Sales (Million Rs)', mode='lines', yaxis='y2', line=dict(color='#4684E3')))

# Customize the chart layout
fig.update_layout(
    title=f'YoY Total Income and Total Sales for {selected_company}',
    xaxis_title='Year',
    yaxis_title='YoY Total Income (%)',
    yaxis2=dict(
        title='Total Sales (Million Rs)',
        overlaying='y',
        side='right',
    ),
    legend_title='Metrics',
    yaxis_tickformat=",.2f",  # Format y-axis labels to display values in millions with two decimal places
    yaxis2_tickformat=",.2f",  # Format y-axis labels for the secondary axis
)

st.header(f"Sales - Income Analysis")
# Show the combined chart with dual axes using Streamlit
st.plotly_chart(fig)
################################################################################################################################################################################################sales and Income Plotted

# Extract industry for the selected company
selected_company_industry = financial_data['current_assets'][selected_company]['industry']
industry_avg_pe = financial_data['current_assets'][selected_company]['Industry PE']

# Get all company names in the selected industry
industry_company_names = [company for company, data in financial_data['current_assets'].items() if data.get('industry') == selected_company_industry]

# Sort the company names by the absolute difference in market cap from the selected company
industry_company_names.sort(key=lambda company: abs(financial_data['current_assets'][company]['Market Capitalisation'] - financial_data['current_assets'][selected_company]['Market Capitalisation']))

# Check the number of companies in the industry
if len(industry_company_names) <= 5:
    # Display all companies in the industry
    closest_company_names = industry_company_names
else:
    # Limit the selection to the top 5 closest companies (excluding the selected company itself)
    closest_company_names = industry_company_names[1:6]

# Extract P/E ratios for all companies in the same industry
pe_ratios = []
company_names = []

for company, data in financial_data['current_assets'].items():
    if company != selected_company and data.get('industry') == selected_company_industry and data.get('P/E') is not None:
        pe_ratios.append(data['P/E'])
        company_names.append(company)

# Add the P/E ratio of the selected company to the list
selected_company_pe = financial_data['current_assets'][selected_company]['P/E']
pe_ratios.append(selected_company_pe)
company_names.append(selected_company)

# Create lists for the selected companies
selected_company_names = [selected_company] + [f'{selected_company_industry} Average']
selected_company_pes = [selected_company_pe, industry_avg_pe]

# Create lists for the top companies
top_company_names = closest_company_names + selected_company_names
top_company_pes = [financial_data['current_assets'][company]['P/E'] for company in closest_company_names] + selected_company_pes

# Create a DataFrame for the bubble plot with the top companies and adjust the color mapping
bubble_data = pd.DataFrame({
    'Company': top_company_names,
    'P/E Ratio': top_company_pes,
    'Color': ['#469EE3' if company == selected_company else '#E3E046' if company == f'{selected_company_industry} Average' else ('#E34653' if pe > industry_avg_pe else '#46E366') for company, pe in zip(top_company_names, top_company_pes)]
})

# Create a bubble plot using Plotly Express with color mapping and adjust the figure size
fig = px.scatter(bubble_data, x='Company', y='P/E Ratio', size='P/E Ratio', color='Color',
                 labels={'Company': 'Companies', 'P/E Ratio': 'P/E Ratio'},
                 title=f'P/E Ratio Comparison for {selected_company} and Peers in the {selected_company_industry} Industry',
                 hover_name='Company',
                 color_discrete_map={'#E3DC46': '#E3DC46', '#469EE3': '#469EE3', '#46E366': '#46E366', '#E34653': '#E34653', '#E3E046': '#E3E046'})

# Customize the appearance of the bubble plot
fig.update_traces(marker=dict(sizemode='diameter'), showlegend=False)

# Set a larger figure size to make all bubbles clearly visible
fig.update_layout(width=1000, height=600)  # Adjust width and height as needed

# Zoom out the plot a bit
fig.update_xaxes(range=[-1, len(company_names)], title_text='Companies')

# Display statement based on P/E comparison outside the plot
if selected_company_pe > industry_avg_pe:
    statement = f"{selected_company} has a higher P/E than the industry average"
    symbol = "⬆️"
else:
    statement = f"{selected_company} has a lower P/E than the industry average"
    symbol = "⬇️"

# Add annotation to display the statement with colored symbol outside the plot

st.header(f"PE Ratio")
st.write(f"**{statement}** {symbol}", unsafe_allow_html=True)
st.plotly_chart(fig)

################################################################################################################################################################################## PE Plotted
# Extract industry for the selected company
selected_company_industry = financial_data['current_assets'][selected_company]['industry']
industry_avg_pb = financial_data['current_assets'][selected_company]['Industry PB']

# Get all company names in the selected industry
industry_company_names = [company for company, data in financial_data['current_assets'].items() if data.get('industry') == selected_company_industry]

# Sort the company names by the absolute difference in market cap from the selected company
industry_company_names.sort(key=lambda company: abs(financial_data['current_assets'][company]['Market Capitalisation'] - financial_data['current_assets'][selected_company]['Market Capitalisation']))

# Check the number of companies in the industry
if len(industry_company_names) <= 5:
    # Display all companies in the industry
    closest_company_names = industry_company_names
else:
    # Limit the selection to the top 5 closest companies (excluding the selected company itself)
    closest_company_names = industry_company_names[1:6]

# Extract P/B ratios for all companies in the same industry
pb_ratios = []
company_names = []

for company, data in financial_data['current_assets'].items():
    if company != selected_company and data.get('industry') == selected_company_industry and data.get('P/B') is not None:
        pb_ratios.append(data['P/B'])
        company_names.append(company)

# Add the P/B ratio of the selected company to the list
selected_company_pb = financial_data['current_assets'][selected_company]['P/B']
pb_ratios.append(selected_company_pb)
company_names.append(selected_company)
# Create lists for the selected companies
selected_company_names = [selected_company] + [f'{selected_company_industry} Average']
selected_company_pbs = [selected_company_pb, industry_avg_pb]

# Create lists for the top companies
top_company_names = closest_company_names + selected_company_names
top_company_pbs = [financial_data['current_assets'][company]['P/B'] for company in closest_company_names] + selected_company_pbs

# Create a DataFrame for the bubble plot with the top companies and adjust the color mapping
bubble_data = pd.DataFrame({
    'Company': top_company_names,
    'P/B Ratio': top_company_pbs,
    'Color': ['#469EE3' if company == selected_company else '#E3E046' if company == f'{selected_company_industry} Average' else ('#E34653' if pb > industry_avg_pb else '#46E366') for company, pb in zip(top_company_names, top_company_pbs)]
})

# Create a bubble plot using Plotly Express with color mapping and adjust the figure size
fig = px.scatter(bubble_data, x='Company', y='P/B Ratio', size='P/B Ratio', color='Color',
                 labels={'Company': 'Companies', 'P/B Ratio': 'P/B Ratio'},
                 title=f'P/B Ratio Comparison for {selected_company} and Peers in the {selected_company_industry} Industry',
                 hover_name='Company',
                 color_discrete_map={'#E3DC46': '#E3DC46', '#469EE3': '#469EE3', '#46E366': '#46E366', '#E34653': '#E34653', '#E3E046': '#E3E046'})

# Customize the appearance of the bubble plot
fig.update_traces(marker=dict(sizemode='diameter'), showlegend=False)

# Set a larger figure size to make all bubbles clearly visible
fig.update_layout(width=1000, height=600)  # Adjust width and height as needed

# Zoom out the plot a bit
fig.update_xaxes(range=[-1, len(company_names)], title_text='Companies')

# Display statement based on P/B comparison outside the plot
if selected_company_pb > industry_avg_pb:
    statement = f"{selected_company} has a higher P/B than the industry average"
    symbol = "⬆️"
else:
    statement = f"{selected_company} has a lower P/B than the industry average"
    symbol = "⬇️"

# Add annotation to display the statement with colored symbol outside the plot
st.header('PB Ratio')
st.write(f"**{statement}** {symbol}", unsafe_allow_html=True)
st.plotly_chart(fig)
#####################################################################################################################################################################PB Bubble plotted
# Define common columns for both tables
st.header('Company at Glance')
common_columns = [
    'ticker', 'industry', 'NIFTY closing', 'Date', 'Market Capitalisation',
    'EPS', 'P/E', 'P/B', 'Beta', 'Industry PE', 'Industry PB', 'Risk_Score', 'risk',
    '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'
]
fund_columns = ['ticker', 'Market Capitalisation',
    'EPS', 'P/E', 'P/B', 'Beta']
# Create a DataFrame for Fundamentals Peers Comparison
# Extract industry for the selected company
selected_company_industry = financial_data['current_assets'][selected_company]['industry']
industry_avg_pb = financial_data['current_assets'][selected_company]['Industry PB']

# Get all company names in the selected industry
industry_company_names = [company for company, data in financial_data['current_assets'].items() if data.get('industry') == selected_company_industry]

# Sort the company names by the absolute difference in market cap from the selected company
industry_company_names.sort(key=lambda company: abs(financial_data['current_assets'][company]['Market Capitalisation'] - financial_data['current_assets'][selected_company]['Market Capitalisation']))

# Check the number of companies in the industry
if len(industry_company_names) <= 5:
    # Display all companies in the industry
    closest_company_names = industry_company_names
else:
    # Limit the selection to the top 5 closest companies (excluding the selected company itself)
    closest_company_names = industry_company_names[1:6]
fundamentals_data = []
for company, data in financial_data['current_assets'].items():
    if company == selected_company or company in closest_company_names:
        row = [data[column] for column in fund_columns]
        fundamentals_data.append(row)

fundamentals_df = pd.DataFrame(fundamentals_data, columns=fund_columns)

# Create a DataFrame for the financials of the selected company
financials_data = []
for metric, data in financial_data.items():
    if selected_company in data:
        row = [metric] + [data[selected_company].get(year, None) for year in years]
        financials_data.append(row)

# Create a DataFrame for financials
financials_df = pd.DataFrame(financials_data, columns=['Metric'] + years)

# Create Streamlit radio buttons for selecting the table type
table_type = st.radio("Select a table:", ["Fundamentals Peers Comparison", "Financials of Selected Company"])

# Display the selected table
if table_type == "Financials of Selected Company":
    st.table(financials_df)
else:
    st.table(fundamentals_df)
############################################################################################################################################tables plotted     
# Add an empty Markdown element to create some space
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")


st.write('<div style="text-align: right;"><span style="font-weight: bold; font-size: larger;">Submitted by Group 5</span></div>', unsafe_allow_html=True)
