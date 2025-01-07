import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
import requests
import plotly.express as px

st.title('Diabetes Pandemic')



AGE_COLUMN = 'Age'
DATA_URL = ('https://raw.githubusercontent.com/jonathann247/diabetesapp/refs/heads/main/diabetes.csv')



# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load data into the dataframe.
s=requests.get(DATA_URL).text
data = pd.read_csv(StringIO(s))
st.write(data)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Diabetes data")





st.subheader('Diabetes By Age')

hist_values = np.histogram(data[AGE_COLUMN], bins=10, range=(0,70))[0]

st.bar_chart(hist_values)

st.subheader('BMI By Age')

fig = px.scatter(data,x='Age', y='BMI', color='Outcome', size='DiabetesPedigreeFunction')
event = st.plotly_chart(fig,key="iris", on_select="rerun")


event.selection

st.subheader('Blood-Pressure Outcome By Age')
st.bar_chart(data, x='Age', y='BloodPressure', color='Outcome')

st.subheader('Blood-Pressure Outcome By Pregnancies')
st.bar_chart(data, x='Pregnancies', y='BloodPressure', color='Outcome', stack=False)


st.subheader('Glucose by Age and Pregnancies')
st.bar_chart(data, x='Age', y='Glucose', color='Pregnancies', stack=False)



