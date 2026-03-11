import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv("parkinson.csv")

# Prepare features and target
X = data.drop(['subject#','motor_UPDRS','total_UPDRS'], axis=1)
y = data['total_UPDRS']

# Train model
model = RandomForestRegressor()
model.fit(X, y)

st.title("Parkinson Disease Severity Prediction")

st.write("Enter patient voice features")

age = st.number_input("Age")
sex_option = st.selectbox("Sex", ["Male", "Female"])

# Convert text to numeric
sex = 1 if sex_option == "Male" else 0

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
                                jitter, shimmer, nhr,
                                hnr, rpde, dfa, ppe]],
                                columns=X.columns)

    prediction = model.predict(input_data)

    st.success(f"Predicted Parkinson Severity: {prediction[0]}")