#import libraries 
import streamlit as st
import pandas as pd
import numpy as np


#title
st.title("""ClaimCatcher
         automated fraud detection in medical insurance claims
         """)


#display some text 
st.text ("App that will show whether a claim is fraudulent or not")

#fetch some data
df = pd.read_csv("ClaimExport.csv")

@st.cache
def load_data(nrows):
    data = pd.read_csv("ClaimExport.csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis = "columns", inplace = True)
    return data


# Create a text element and let the reader know the data is loading.
#data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
#data_load_state.text("Done! (using st.cache)")


#inspect the raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data["total_amount"])

#draw a histogram
st.subheader('Amount claimed for each submitted claim')
st.bar_chart(data["total_amount"])

st.subheader('Amount approved for each submitted claim')
st.bar_chart(data["approved_amount"])
                  
                  
                  
                  
                  