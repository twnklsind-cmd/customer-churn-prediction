import streamlit as st
import pandas as pd
import numpy as np
import joblib

model=joblib.load('models/churn_model.pkl')
scaler=joblib.load('models/scaler.pkl')

st.set_page_config(page_title="Churn Predictor", page_icon="📉")
st.title("Churn Predictor")
st.write("Fill in the customer details to predict if they churn")

col1, col2= st.columns(2)

with col1:
    tenure=st.slider("Tenure(months)", 0, 72, 12)
    monthly_charges=st.number_input("Monthly charges($)", 0.0, 200.0, 65.0)
    total_charges=monthly_charges*tenure

with col2:
    contract=st.selectbox("Contract Type", ["Month-to-Month", "One Year", "Two Year"])
    internet=st.selectbox("Internet Service", ["DSL", "Fibre optic", "No"])
    tech_support=st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    senior=st.selectbox("Senior Citizen", ["No", "Yes"])

st.write(f"Total Charges(auto-calculated): **${total_charges:.2f}**")

contract_map={"Month-to-Month":0, "One Year":1, "Two Year":2}
internet_map={"DSL":0, "Fibre optic":1, "No":2}
support_map={"Yes":0, "No":1, "No internet service":2}
senior_map={"No":0, "Yes":1}

input_df=pd.DataFrame([{
    'gender':0,
    'SeniorCitizen':senior_map[senior],
    'Partner':0,
    'Dependents':0,
    'tenure':tenure,
    'PhoneService':1,
    'MultipleLines':0,
    'InternetService':internet_map[internet],
    'OnlineSecurity':0,
    'OnlineBackup':0,
    'DeviceProtection':0,
    'TechSupport':support_map[tech_support],
    'StreamingTV':0,
    'StreamingMovies':0,
    'Contract':contract_map[contract],
    'PaperlessBilling':1,
    'PaymentMethod':0,
    'MonthlyCharges':monthly_charges,
    'TotalCharges':total_charges
}])

input_scaled=scaler.transform(input_df)

if st.button("Predict Churn"):
    prediction=model.predict(input_scaled)[0]
    probability=model.predict_proba(input_scaled)[0][1]

    st.divider()
    if prediction==1:
        st.error(f"This customer is **likely to churn !**")
        st.metric("Churn Probability :", f"{probability:.0%}")
    else:
        st.success(f"THis customer is **likely to stay.**")
        st.metric("Churn Probability :", f"{probability:.0%}")
