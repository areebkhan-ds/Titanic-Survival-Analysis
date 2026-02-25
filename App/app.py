import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("titanic_model.pkl")

# Page config
st.set_page_config(page_title="Titanic Survival App", page_icon="🚢", layout="centered")

# Custom CSS: faded background + black labels + button
st.markdown(
    """
    <style>
    /* Background image with low opacity */
    .stApp {
        background: linear-gradient(rgba(255,255,255,0.7), rgba(255,255,255,0.7)),
                    url("https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg");
        background-size: cover;
        background-position: center;
    }

    /* Make all labels black */
    label, .stMarkdown {
        color: black !important;
        font-weight: bold;
    }

    /* Red button styling */
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        font-size: 18px;
        height: 50px;
        width: 100%;
        border-radius: 10px;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title using HTML (works reliably)
st.markdown('<h1 style="color:black;">🚢 Titanic Survival Prediction</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="color:black;">Will this passenger survive the Titanic disaster?</h3>', unsafe_allow_html=True)

# Input columns
col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("Passenger Class", [1, 2, 3])
    sex = st.selectbox("Sex", ["male", "female"])
    age = st.slider("Age", 0, 80, 25)
    sibsp = st.number_input("Siblings/Spouses Aboard", 0, 8, 0)

with col2:
    parch = st.number_input("Parents/Children Aboard", 0, 6, 0)
    fare = st.number_input("Fare", 0.0, 500.0, 50.0)
    embarked = st.selectbox("Embarked Port", ["C", "Q", "S"])

# Encode categorical features
sex = 1 if sex == "male" else 0
embarked_map = {"C": 0, "Q": 1, "S": 2}
embarked = embarked_map[embarked]

# Prediction button
if st.button("Predict Survival"):
    features = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])
    prediction = model.predict(features)

    st.markdown("---")  # horizontal line

    if prediction[0] == 1:
        st.success("🎉 This passenger is likely to SURVIVE!")
    else:
        st.error("❌ This passenger is NOT likely to survive.")