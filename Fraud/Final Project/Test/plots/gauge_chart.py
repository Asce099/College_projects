import plotly.graph_objects as go
import streamlit as st

def create_gauge_chart(selected_company, selected_company_risk):
    # Create a gauge chart using Plotly
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=selected_company_risk,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Risk Rating"},
        gauge={
            'axis': {'range': [0, 4], 'tickwidth': 1, 'tickcolor': "black"},
            'bar': {'color': "black"},
            'steps': [
                {'range': [0, 1], 'color': "#D60A2A"},
                {'range': [1, 2], 'color': "#F6C420"},
                {'range': [2, 3], 'color': "#59E34C"},
                {'range': [3, 4], 'color': "#4699E3"}
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

    # Display the decoded risk rating
    st.write(f"{risk_labels[selected_company_risk]}")

    # Show the gauge chart
    st.plotly_chart(fig)


