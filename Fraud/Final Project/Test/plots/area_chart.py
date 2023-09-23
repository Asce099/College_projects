import plotly.express as px
import pandas as pd
import streamlit as st

def create_area_chart(selected_company, selected_company_data, financial_metrics_columns, years):
    # Create a DataFrame for the selected company's data
    selected_company_data = pd.DataFrame({
        'Year': years,
        'Yield': [selected_company_data['yield'][selected_company][year] for year in years],
        'Turnover': [selected_company_data['turnover'][selected_company][year] for year in years]
    })

    # Create an area chart for Yield and Turnover
    fig = px.area(
        selected_company_data,
        x='Year',
        y=financial_metrics_columns,
        title=f'{", ".join(financial_metrics_columns)} Over the Years for {selected_company}',
        labels={'Year': 'Year', 'value': 'Value'},
        width=800, height=400,
        color_discrete_map={'Yield': '#4699E3', 'Turnover': '#46E36E'}
    )

    # Customize the chart layout (optional)
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Value',
        legend_title='Metrics',
    )

    # Show the area chart
    st.plotly_chart(fig)
