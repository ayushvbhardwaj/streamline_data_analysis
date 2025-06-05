import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv("student-mat.csv", delimiter=';')

st.title("Student Performance Analysis")

st.header("Raw Data")
st.dataframe(data)

st.header("Summary Statistics")
st.write(data.describe(include='all'))

st.header("Polulation with respect to gender")
fig_sex_pie = px.pie(data, names='sex', title="Percentage of Students by Gender")
st.plotly_chart(fig_sex_pie)

st.header("Distribution of Students by Age")
fig_age = px.histogram(data, x="age", nbins=20, title="Age Distribution of Students")
st.plotly_chart(fig_age)

st.header("Distribution of Students by home location")
fig_loc = px.pie(data, names='address', title="Percentage of Students by Home Location")
st.plotly_chart(fig_loc)

