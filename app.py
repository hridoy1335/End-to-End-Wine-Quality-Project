import pandas as pd
import streamlit as st
from src.wine.utils import load_obj
from src.wine.config.configuration import *
from src.wine.pipeline.prediction_pipeline import ModelPredictionPipeliene


st.title("WINE QUALITY PREDICTION")
st.write("This is a web application for wine quality prediction.")
fixed_acidity = st.number_input("Enter the fixed acidity value")
volatile_acidity = st.number_input("Enter the volatile acidity value")
citric_acid = st.number_input("Enter the citric acid value")
residual_sugar = st.number_input("Enter the residual sugar value")
chlorides = st.number_input("Enter the chlorides value")
free_sulfur_dioxide = st.number_input("Enter the free sulfur dioxide value")
total_sulfur_dioxide = st.number_input("Enter the total sulfur dioxide value")
density = st.number_input("Enter the density value")
pH = st.number_input("Enter the pH value")
sulphates = st.number_input("Enter the sulphates value")
alcohol = st.number_input("Enter the alcohol value")


data = [[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]]



if st.button("Predict"):
    model = load_obj(file_path="artifacts/2025-06-03-04:17:42/model/model.pkl")
    pred = model.predict(data)
    st.write(f"predicted quality is {pred}")  # display the result