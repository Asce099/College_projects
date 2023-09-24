import plotly.express as px
import streamlit as st

def plot_line_chart(data, years, selected_company):
    st.write("YoY Financial Data for Selected Company:")
    for key, df in data.items():
        selected_data = df[selected_company]
        fig = px.line(x=years, y=[selected_data[year] for year in years], title=key)
        st.plotly_chart(fig)


