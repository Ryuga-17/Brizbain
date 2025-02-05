
import streamlit as st

# Define options for the select boxes
options = ["Option 1", "Option 2", "Option 3"]

# Create columns for horizontal alignment
col1, col2, col3 = st.columns(3)

# Add select boxes to the columns with the same options
with col1:
    selected1 = st.selectbox("Select Box 1", options)

with col2:
    selected2 = st.selectbox("Select Box 2", options)

with col3:
    selected3 = st.selectbox("Select Box 3", options)

# Display the selected options
st.write("You selected:", selected1, selected2, selected3)
