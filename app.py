import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("./models/lr_model.pkl", "rb"))

# Page config
st.set_page_config(page_title="Used Car Price Prediction", page_icon="🚗", layout="centered")

# Title and Image
st.image("static/price.png")
st.title("Flora's Used Car Price Prediction App")

# User Inputs
km = st.number_input("Enter kilometers (Kms)", min_value=2000, max_value=1000000, value=None)
age = st.number_input("Enter car age (years)", min_value=0, max_value=100, value=None)
oprice = st.number_input("Enter original price (R)", min_value=10000, max_value=10000000, value=None)

fuel_type = st.selectbox("Select Fuel Type", ["Petrol", "Diesel", "CNG"])
transmission = st.selectbox("Select Transmission", ["Manual", "Automatic"])

# Encoding fuel type
if fuel_type == "Petrol":
    fuel = [0.0, 0.0, 1.0]
elif fuel_type == "Diesel":
    fuel = [0.0, 1.0, 0.0]
else:  # CNG
    fuel = [1.0, 0.0, 0.0]

# Encoding transmission
if transmission == "Automatic":
    trans = [0.0, 1.0]
else:
    trans = [1.0, 0.0]

# Predict Button
if st.button("Predict Price"):
    data = np.array([oprice, km, age, fuel[0], fuel[1], fuel[2], trans[0], trans[1]])
    result = np.round(model.predict([data]))
    st.success(f"💰 Predicted car price is Rs. {result[0]:,.0f}")
