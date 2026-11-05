import pandas as pd
import streamlit as st
import numpy as np
import joblib
# Load the trained machine learning model
model = joblib.load("gold_price_model.pkl")
# App title
st.title("Gold Price Prediction")

# App description
st.write(
    "This application predicts the next GLD price "
    "using a trained Random Forest model."
)
# Input fields
st.subheader("Enter Financial Indicators")

spx = st.number_input("S&P 500 (SPX)", value=1650.0)
gld = st.number_input("Current GLD Price", value=120.0)
uso = st.number_input("US Oil Fund (USO)", value=32.0)
slv = st.number_input("Silver Price (SLV)", value=20.0)
eur_usd = st.number_input("EUR/USD Exchange Rate", value=1.28)

gld_lag1 = st.number_input("Previous GLD Price", value=120.0)
gld_lag5 = st.number_input("GLD Price 5 Observations Ago", value=119.0)
gld_change1 = st.number_input("GLD Price Change", value=0.5)
# Prediction button
if st.button("Predict Gold Price"):
   input_data = pd.DataFrame([[
    spx,
    gld,
    uso,
    slv,
    eur_usd,
    gld_lag1,
    gld_lag5,
    gld_change1
   ]], columns=[
    'SPX',
    'GLD',
    'USO',
    'SLV',
    'EUR/USD',
    'GLD_Lag1',
    'GLD_Lag5',
    'GLD_Change1'
   ])
   prediction = model.predict(input_data)
   st.success(f"Predicted Next GLD Price: ${prediction[0]:.2f}")
