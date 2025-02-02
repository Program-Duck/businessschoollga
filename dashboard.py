import pandas as pd
import streamlit as st

# Read the CSV files
business_df = pd.read_csv('VIC_business.csv')
school_df = pd.read_csv('VIC_school_data.csv')

# Rename 'LGA_Name' to 'LGA' in the school dataframe for consistency
school_df = school_df.rename(columns={'LGA_Name': 'LGA'})

# Set the page title and layout
st.set_page_config(page_title='LGA Dashboard', layout='wide')

# Create the dropdown for LGA selection
selected_lga = st.selectbox('Select an LGA', business_df['LGA'].unique())

# Create two columns for school data and business data
col1, col2 = st.columns(2)

# Display school data
with col1:
    st.header('School Data')
    if selected_lga:
        filtered_school_df = school_df[school_df['LGA'] == selected_lga]
        st.table(filtered_school_df)

# Display business data
with col2:
    st.header('Business Data')
    if selected_lga:
        filtered_business_df = business_df[business_df['LGA'] == selected_lga]
        st.table(filtered_business_df)