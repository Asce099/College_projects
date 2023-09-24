import streamlit as st
from PyPDF2 import PdfReader
import re
import numpy as np
from collections import defaultdict
import plotly.graph_objs as go
import time

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract digits from text using regular expressions
def extract_digits(text):
    return re.findall(r'\d+', text)

# Function to apply Benford's Law
def apply_benford_law(numbers):
    benford_probs = {str(i): np.log10(1 + 1/i) for i in range(1, 10)}
    observed_counts = defaultdict(int)
    
    for number in numbers:
        first_digit = number[0]
        if first_digit != '0':  # Exclude numbers starting with '0'
            observed_counts[first_digit] += 1
    
    # Ensure that all possible first digits (1-9) are included in the counts
    for i in range(1, 10):
        if str(i) not in observed_counts:
            observed_counts[str(i)] = 0
    
    total_counts = sum(observed_counts.values())
    expected_counts = {str(i): benford_probs[str(i)] * total_counts for i in range(1, 10)}
    
    return observed_counts, expected_counts, total_counts

# Streamlit UI
st.title("Benford Model Testing for Detecting Earning Manipulators")

# File uploader widget
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Set a timeout duration (in seconds) to prevent long processing times
    timeout_duration = 60  # Adjust as needed

    # Use time.time() to keep track of time
    start_time = time.time()

    try:
        # Extract text from the uploaded PDF
        pdf_text = extract_text_from_pdf(uploaded_file)

        # Extract digits from the text
        digits = extract_digits(pdf_text)

        if len(digits) == 0:
            st.warning("No digits found in the PDF.")
        else:
            # Check if the processing time exceeds the timeout duration
            if time.time() - start_time > timeout_duration:
                st.error("Processing took too long. Please upload a smaller PDF.")
            else:
                # Apply Benford's Law
                observed_counts, expected_counts, total_observed_count = apply_benford_law(digits)

                # Calculate total expected count based on Benford's Law
                total_expected_count = sum(expected_counts.values())

                # Determine conclusion based on the total counts
                threshold = 1.96  # 5% level of significance
                z_score = (total_observed_count - total_expected_count) / np.sqrt(total_expected_count)

                # Determine the color of the result based on the conclusion
                result_color = 'red' if abs(z_score) >= threshold else 'green'

                # Display the result
                st.subheader("Conclusion:")
                if abs(z_score) >= threshold:
                    st.write("The data significantly deviates from Benford's Law, indicating potential anomalies (5% level of significance).")
                else:
                    st.write("The data conforms reasonably well to Benford's Law (5% level of significance).")

                # Create a Plotly bar chart for the observed counts with the determined color
                observed_bar = go.Bar(
                    x=list(observed_counts.keys()),
                    y=list(observed_counts.values()),
                    name='Observed',
                    marker=dict(color=result_color)  # Set the color of the result
                )

                # Create a line plot for the actual expected Benford values
                expected_line = go.Scatter(
                    x=list(expected_counts.keys()),
                    y=list(expected_counts.values()),
                    mode='lines+markers',
                    name='Benford\'s Law (Actual)'
                )

                layout = go.Layout(
                    title='Observed vs. Expected Counts (Benford\'s Law)',
                    xaxis=dict(title='First Digit', tickmode='array', tickvals=list(observed_counts.keys())),
                    yaxis=dict(title='Count'),
                    barmode='group'
                )

                fig = go.Figure(data=[observed_bar, expected_line], layout=layout)
                st.plotly_chart(fig)


    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
