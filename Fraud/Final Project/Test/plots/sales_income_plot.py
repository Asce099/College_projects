import plotly.graph_objects as go
import pandas as pd
import streamlit as st

def create_sales_income_plot(selected_company, years, financial_data):
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
        yaxis_tickformat=",.2f",
        yaxis2_tickformat=",.2f",
    )

    # Show the combined chart with dual axes using Streamlit
    st.plotly_chart(fig)
