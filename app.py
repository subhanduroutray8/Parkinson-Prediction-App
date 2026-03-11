import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("parkinson_model.pkl")

st.title("Parkinson Disease Severity Prediction")

st.write("Enter patient voice features")

age = st.number_input("Age")
sex = st.selectbox("Sex", ["Male","Female"])
test_time = st.number_input("Test Time")

jitter = st.number_input("Jitter (%)")
shimmer = st.number_input("Shimmer")
nhr = st.number_input("NHR")
hnr = st.number_input("HNR")
rpde = st.number_input("RPDE")
dfa = st.number_input("DFA")
ppe = st.number_input("PPE")

if st.button("Predict"):

    input_data = pd.DataFrame([[age, sex, test_time,
                                jitter, shimmer, nhr, hnr,
                                rpde, dfa, ppe]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Severity: {prediction[0]}")