import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open('medical_cost_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

# ------------------ Page Setup ------------------
st.set_page_config(page_title="Medical Insurance Cost Predictor", layout="centered")

# ------------------ Dark Theme Styling + Background ------------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(14,17,23,0.85), rgba(14,17,23,0.85)),
                    url('https://img.freepik.com/free-vector/abstract-medical-wallpaper-template-design_53876-61804.jpg');
        background-size: cover;
        background-position: center;
        color: #FAFAFA;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 2.4rem;
        font-weight: bold;
        color: #4db8ff;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #cccccc;
        margin-bottom: 1.5rem;
    }
    .top-image {
        display: flex;
        justify-content: center;
        margin-bottom: 1.5rem;
    }
    .top-image img {
        width: 120px;
        border-radius: 50%;
        box-shadow: 0 0 15px rgba(0,0,0,0.5);
        background-color: #1c1e24;
        padding: 10px;
    }
    .prediction-box {
        background-color: rgba(28,30,36,0.9);
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        box-shadow: 0 0 20px rgba(0,0,0,0.4);
        color: #FAFAFA;
    }
    label, .css-1cpxqw2, .st-bw, .st-cy, .st-em {
        color: #FAFAFA !important;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ Title ------------------
st.markdown("<div class='title'>💊 Medical Insurance Cost Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Estimate your annual insurance cost based on health and lifestyle factors.</div>", unsafe_allow_html=True)

# ------------------ Top Image ------------------
st.markdown("""
<div class="top-image">
    <img src="https://github.com/satyam2006-cmd/Medical-Cost-Prediction-Model-/blob/main/medical_cost_prediction_model.png?raw=true" alt="Medical Cost Predictor Logo">
</div>
""", unsafe_allow_html=True)

# ------------------ Input Layout ------------------
col1, col2 = st.columns(2)

with col1:
    age = st.slider("🎂 Age", 18, 100, 30)
    bmi = st.number_input("⚖️ BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0)
    children = st.selectbox("👶 Number of Children", list(range(6)))

with col2:
    sex = st.selectbox("🧑 Sex", ["male", "female"])
    smoker = st.selectbox("🚬 Smoker", ["yes", "no"])
    region = st.selectbox("🌍 Region", ["southeast", "southwest", "northeast", "northwest"])

# ------------------ Encode Inputs ------------------
sex_encoded = 1 if sex == "male" else 0
smoker_encoded = 1 if smoker == "yes" else 0
region_map = {"southeast": 0, "southwest": 1, "northeast": 2, "northwest": 3}
region_encoded = region_map[region]

input_data = pd.DataFrame({
    'age': [age],
    'sex': [sex_encoded],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker_encoded],
    'region': [region_encoded]
})

# ------------------ Predict & Display ------------------
if st.button("📊 Predict Insurance Cost"):
    try:
        prediction = model.predict(input_data)[0]
        st.markdown(f"""
            <div class="prediction-box">
                <h3>💰 Estimated Cost: <span style="color:#2b8a3e">${prediction:,.2f}</span></h3>
                <p>Based on the provided information, this is the estimated annual medical insurance cost.</p>
            </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error making prediction: {e}")
