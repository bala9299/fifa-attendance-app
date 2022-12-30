import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import altair as alt
st.set_option('deprecation.showPyplotGlobalUse', False)

df=pd.read_csv("data//fifa_wca.csv")
st.title("FIFA World Cup Attendance")
navigate=st.sidebar.radio("FIFA",["Years","Total attendance","Add attendance"])

if navigate == "Years":
    st.image("data\\fifa.jpg")
    if st.checkbox("Show dataframe"):
        st.dataframe(df)
    year = st.selectbox("Select a year",df.Year,0)
    attendance = df.loc[df.Year==year]["Total_Attendance"].iloc[0]
    place = df.loc[df.Year==year]["Hosts"].iloc[0]
    venue = df.loc[df.Year==year]["Venue"].iloc[0]
    matches = df.loc[df.Year==year]["Matches"].iloc[0]
    finals = df.loc[df.Year==year]["Game(s)"].iloc[0]
    st.write(f'Total Attendance : {attendance}.')
    st.write(f'The worldcup was hosted by : {place}.')
    st.write(f'Number of matched played : {matches}.')
    st.write(f'The results of final match : {finals}.')
    st.write(f'Where was the finals played : {venue}.')

if navigate == "Total attendance":
    st.write("Total attendance = ", df["Total_Attendance"].sum())
    plt.title("Total Attendance")
    plt.figure(figsize=(12,12))
    att= pd.DataFrame(df['Total_Attendance'])
    st.bar_chart(att)
if navigate == "Add attendance":
    st.header("This will add in our dataset")
    col1 = st.number_input("Enter the year")
    col2 = st.text_input("Who hosted the worldcup")
    col3 = st.number_input("Enter the total number of attendance")
    col4 = st.number_input("Enter the total number matches")
    col5 = st.number_input("Enter the average number of attendance")
    col6 = st.text_input("Enter the stadium name")
    col7 = st.text_input("the final match result")
    if st.button("submit"):
        new_data = {"Year":col1, "Hosts":col2, "Total_Attendance":col3, "Matches":col4, "Average_Attendance":col5,
                "Venue":col6, "Game(s)":col7}
        st.write(new_data)
        df=df.append(new_data,ignore_index=True) 
        df.to_csv("data//fifa_wca.csv",header=True)       
        st.success("submitted")    