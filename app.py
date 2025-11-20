import pandas as pd
import joblib
import streamlit as st


model = joblib.load("churn_model.pkl")


sample = pd.read_csv("sample_features.csv")  

st.title("Customer Churn Prediction App")

st.write("Enter customer details to predict churn.")


gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure", min_value=0, max_value=100)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)




input_data = {
    "gender_Female": 1 if gender == "Female" else 0,
    "gender_Male": 1 if gender == "Male" else 0,
    "SeniorCitizen": senior,
    "Partner_Yes": 1 if partner == "Yes" else 0,
    "Partner_No": 1 if partner == "No" else 0,
    "Dependents_Yes": 1 if dependents == "Yes" else 0,
    "Dependents_No": 1 if dependents == "No" else 0,
    "tenure": tenure,
    "PhoneService_Yes": 1 if phone_service == "Yes" else 0,
    "PhoneService_No": 1 if phone_service == "No" else 0,

    # New categories
    "MultipleLines_Yes": 1 if multiple_lines == "Yes" else 0,
    "MultipleLines_No": 1 if multiple_lines == "No" else 0,
    "MultipleLines_No phone service": 1 if multiple_lines == "No phone service" else 0,

    "InternetService_DSL": 1 if internet_service == "DSL" else 0,
    "InternetService_Fiber optic": 1 if internet_service == "Fiber optic" else 0,
    "InternetService_No": 1 if internet_service == "No" else 0,

    "OnlineSecurity_Yes": 1 if online_security == "Yes" else 0,
    "OnlineSecurity_No": 1 if online_security == "No" else 0,
    "OnlineSecurity_No internet service": 1 if online_security == "No internet service" else 0,

    "OnlineBackup_Yes": 1 if online_backup == "Yes" else 0,
    "OnlineBackup_No": 1 if online_backup == "No" else 0,
    "OnlineBackup_No internet service": 1 if online_backup == "No internet service" else 0,

    "DeviceProtection_Yes": 1 if device_protection == "Yes" else 0,
    "DeviceProtection_No": 1 if device_protection == "No" else 0,
    "DeviceProtection_No internet service": 1 if device_protection == "No internet service" else 0,

    "TechSupport_Yes": 1 if tech_support == "Yes" else 0,
    "TechSupport_No": 1 if tech_support == "No" else 0,
    "TechSupport_No internet service": 1 if tech_support == "No internet service" else 0,

    "Contract_Month-to-month": 1 if contract == "Month-to-month" else 0,
    "Contract_One year": 1 if contract == "One year" else 0,
    "Contract_Two year": 1 if contract == "Two year" else 0,

    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
}

input_df = pd.DataFrame([input_data])

# --------- FIX MISSING COLUMNS ----------
# Make sure input_df has same columns as training
missing_cols = set(sample.columns) - set(input_df.columns)

for col in missing_cols:
    input_df[col] = 0


input_df = input_df[sample.columns]


if st.button("Predict"):
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠ Customer will CHURN!")
    else:
        st.success("✔ Customer will NOT churn.")
