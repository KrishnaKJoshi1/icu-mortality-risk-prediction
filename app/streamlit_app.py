import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Title
# -----------------------------
st.title("ICU Mortality Risk Predictor")
st.write("Select a patient record to generate mortality risk scoring.")

# -----------------------------
# Upload Dataset
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload ICU Patient Dataset (CSV)",
    type="csv"
)

# -----------------------------
# Load Model
# -----------------------------

model = joblib.load("artifacts/pipeline.pkl")

# -----------------------------
# If file uploaded
# -----------------------------
if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # -----------------------------
    # Dropdown Row Selection
    # -----------------------------
    row_index = st.selectbox(
        "Select Patient Row",
        options=df.index
    )

    patient = df.iloc[[row_index]]

    st.subheader("Selected Patient Record")
    st.dataframe(patient)

    # -----------------------------
    # Predict Button
    # -----------------------------
    if st.button("Predict Mortality Risk"):

        # Predict probability
        proba = model.predict_proba(patient)[:, 1][0]

        # -----------------------------
        # Risk Level Logic
        # -----------------------------
        if proba < 0.05:
            risk = "Low Risk"
            color = "green"
            message = "Continue standard monitoring."

        elif proba < 0.15:
            risk = "Moderate Risk"
            color = "orange"
            message = "Increase observation frequency."

        elif proba < 0.30:
            risk = "Elevated Risk"
            color = "red"
            message = "Consider clinical review."

        else:
            risk = "Critical Risk"
            color = "darkred"
            message = "Immediate clinical attention required."

        # -----------------------------
        # Output Display
        # -----------------------------
        st.subheader("Risk Output")

        st.metric(
            label="Mortality Probability",
            value=round(proba, 3)
        )

        st.markdown(
            f"### Risk Level: <span style='color:{color}'>{risk}</span>",
            unsafe_allow_html=True
        )

        st.write(f"**Recommendation:** {message}")

        st.caption(
            "Threshold tuned for high Recall to minimize missed high-risk patients."
        )





















