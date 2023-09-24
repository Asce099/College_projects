import plotly.express as px
import pandas as pd
import streamlit as st

def create_pb_comparison_plot(selected_company, financial_data, years):
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
    fig.update_layout(width=1000, height=600)

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
    st.plotly_chart(fig)
    st.markdown(f"**{statement}** {symbol}", unsafe_allow_html=True)
