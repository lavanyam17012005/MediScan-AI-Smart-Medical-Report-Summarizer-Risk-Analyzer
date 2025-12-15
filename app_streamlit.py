import streamlit as st
import pickle
import pandas as pd
from utils.analyzer import check_ranges
from utils.explainer import explain

# Load ML model
with open("model/risk_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🧠 AI Medical Report Summarizer")
st.write("Understand lab reports using AI (Educational use only)")

# User Inputs
glucose = st.number_input("Glucose (mg/dL)", min_value=0.0)
hemoglobin = st.number_input("Hemoglobin (g/dL)", min_value=0.0)
cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=0.0)

if st.button("Analyze Report"):
    values = {
        "glucose": glucose,
        "hemoglobin": hemoglobin,
        "cholesterol": cholesterol
    }

    # Rule-based analysis
    range_results = check_ranges(values)

    st.subheader("🔍 Test Analysis")
    for test, status in range_results.items():
        st.write(f"**{test.capitalize()}**: {status}")
        st.caption(explain(test, status))

    # ML Risk Prediction
    input_df = pd.DataFrame([[glucose, hemoglobin, cholesterol]],
                            columns=["glucose", "hemoglobin", "cholesterol"])

    risk_pred = model.predict(input_df)[0]

    risk_map = {
        0: "🟢 Low Risk",
        1: "🟡 Medium Risk",
        2: "🔴 High Risk"
    }

    st.subheader("📊 Overall Health Risk")
    st.success(risk_map[risk_pred])
