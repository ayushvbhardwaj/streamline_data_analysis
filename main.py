
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
train = pd.read_csv("titanic/train.csv")

st.title("Titanic Data Analysis")

st.header("Raw Data")
st.dataframe(train)


st.header("Summary Statistics")
st.write(train.describe(include='all'))

# Gender distribution
st.header("Gender Distribution")
fig_sex = px.histogram(train, x="Sex", color="Sex", title="Count of Passengers by Gender")
st.plotly_chart(fig_sex)

st.header("Gender Percentage")
fig_sex_pie = px.pie(train, names="Sex", title="Percentage of Passengers by gender", )
st.plotly_chart(fig_sex_pie)

# Survival by gender
st.header("Survival by Gender")
fig_surv_sex = px.histogram(train, x="Sex", color="Survived", barmode="group",
                            title="Survival Count by Gender",
                            category_orders={"Survived": [0, 1]},
                            labels={"Survived": "Survived (0=No, 1=Yes)"})
st.plotly_chart(fig_surv_sex)

# Age distribution
st.header("Age Distribution")
fig_age = px.histogram(train, x="Age", nbins=100, title="Age Distribution")
st.plotly_chart(fig_age)

# Survival by class
st.header("Survival by Passenger Class")
fig_class = px.histogram(train, x="Pclass", color="Survived", barmode="group",
                         title="Survival Count by Passenger Class",
                         category_orders={"Survived": [0, 1]},
                         labels={"Survived": "Survived (0=No, 1=Yes)"})
st.plotly_chart(fig_class)