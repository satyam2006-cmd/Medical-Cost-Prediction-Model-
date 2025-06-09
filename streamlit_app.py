
import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open('medical_cost_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

# ------------------ Page Setup ------------------
st.set_page_config(page_title="Medical Insurance Cost Predictor", layout="centered")

# ------------------ Theme Toggle ------------------
theme = st.selectbox("🎨 Choose Theme", ["Light", "Dark"], index=1)

if theme == "Dark":
    st.markdown("""
        <style>
        .stApp {
            background-color: #0e1117;
            color: #FAFAFA;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            font-size: 2.2rem;
            font-weight: bold;
            color: #4db8ff;
        }
        .prediction-box {
            background-color: #1c1e24;
            padding: 20px;
            border-radius: 12px;
            margin-top: 20px;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
            color: #FAFAFA;
        }
        label, .css-1cpxqw2, .st-bw, .st-cy, .st-em {
            color: #FAFAFA !important;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp {
            font-family: 'Segoe UI', sans-serif;
            background-color: #ffffff;
            color: #000000;
            padding: 2rem;
        }
        .title {
            font-size: 2.2rem;
            font-weight: bold;
            color: #3366cc;
        }
        .prediction-box {
            background-color: #e8f0fe;
            padding: 20px;
            border-radius: 12px;
            margin-top: 20px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)

# ------------------ Title ------------------
st.markdown("<div class='title'>💊 Medical Insurance Cost Predictor</div>", unsafe_allow_html=True)
st.markdown("Use this simple tool to estimate medical insurance costs based on personal health details.")
st.image("https://github.com/satyam2006-cmd/Medical-Cost-Prediction-Model-/blob/main/medical_cost_prediction_model.png?raw=true", width=80)
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
