import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv("parkinson.csv")

# Prepare features and target
X = data.drop(['subject#','motor_UPDRS','total_UPDRS'], axis=1)
y = data[['motor_UPDRS','total_UPDRS']]

# Train model
model = RandomForestRegressor()
model.fit(X, y)

st.title("Parkinson Disease Severity Prediction")

st.write("Enter patient voice features")

age = st.number_input("Age")

sex_option = st.selectbox("Sex", ["Male", "Female"])
sex = 1 if sex_option == "Male" else 0

test_time = st.number_input("Test Time", format="%.5f")

jitter_percent = st.number_input("Jitter (%)", format="%.5f")
jitter_abs = st.number_input("Jitter (Abs)", format="%.5f")
jitter_rap = st.number_input("Jitter RAP", format="%.5f")
jitter_ppq5 = st.number_input("Jitter PPQ5", format="%.5f")
jitter_ddp = st.number_input("Jitter DDP", format="%.5f")

shimmer = st.number_input("Shimmer", format="%.5f")
shimmer_db = st.number_input("Shimmer (dB)", format="%.5f")
shimmer_apq3 = st.number_input("Shimmer APQ3", format="%.5f")
shimmer_apq5 = st.number_input("Shimmer APQ5", format="%.5f")
shimmer_apq11 = st.number_input("Shimmer APQ11", format="%.5f")
shimmer_dda = st.number_input("Shimmer DDA", format="%.5f")

nhr = st.number_input("NHR", format="%.5f")
hnr = st.number_input("HNR", format="%.5f")
rpde = st.number_input("RPDE", format="%.5f")
dfa = st.number_input("DFA", format="%.5f")
ppe = st.number_input("PPE", format="%.5f")


if st.button("Predict"):

    input_data = pd.DataFrame([[

        age,
        sex,
        test_time,
        jitter_percent,
        jitter_abs,
        jitter_rap,
        jitter_ppq5,
        jitter_ddp,
        shimmer,
        shimmer_db,
        shimmer_apq3,
        shimmer_apq5,
        shimmer_apq11,
        shimmer_dda,
        nhr,
        hnr,
        rpde,
        dfa,
        ppe

    ]], columns=X.columns)

    prediction = model.predict(input_data)

    motor = prediction[0][0]
    total = prediction[0][1]

    st.success(f"Predicted Motor UPDRS: {motor:.2f}")
    st.success(f"Predicted Total UPDRS: {total:.2f}")