import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("LinearRegressionModel.pkl", "rb"))

st.title("🚗 Car Price Predictor")

name = st.text_input("Car Name")
company = st.text_input("Company")
year = st.number_input("Year", 1990, 2026)
kms_driven = st.number_input("Kilometers Driven", 0)
fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG", "LPG"]
)

if st.button("Predict"):

    sample = pd.DataFrame({
        'name': [name],
        'company': [company],
        'year': [year],
        'kms_driven': [kms_driven],
        'fuel_type': [fuel_type]
    })

    prediction = model.predict(sample)[0]

    st.success(f"Estimated Price: ₹{prediction:,.0f}")