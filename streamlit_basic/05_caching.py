import streamlit as st
import pandas as pd

@st.cache_data
def load_data(url):
    df = pd.read_csv(url, nrows=1000)
    st.write(df.shape)
    st.write(df.columns)
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")