import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("LinearRegressionModel.pkl", "rb"))

car_names = pickle.load(open("car_names.pkl", "rb"))
companies = pickle.load(open("companies.pkl", "rb"))

st.title("🚗 Car Price Prediction Dashboard")

car_name = st.selectbox(
    "Select Car",
    car_names
)

company = st.selectbox(
    "Select Company",
    companies
)

year = st.number_input(
    "Year",
    min_value=1995,
    max_value=2025
)

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "LPG", "CNG"]
)

if st.button("Predict Price"):

    sample = pd.DataFrame({
        'name': [car_name],
        'company': [company],
        'year': [year],
        'kms_driven': [kms_driven],
        'fuel_type': [fuel_type]
    })

    st.write(sample)
    prediction = model.predict(sample)[0]

    st.success(
        f"Estimated Price: ₹ {prediction:,.0f}"
    )
