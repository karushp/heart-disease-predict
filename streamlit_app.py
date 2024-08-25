import streamlit as st
import pandas as pd

# Import the final pipeline
from data_prep import final_pipeline

# Set page title and icon
st.set_page_config(page_title="Heart Disease Prediction", page_icon="🫀", layout="wide")
st.markdown('<p class="custom-title">Heart Disease Prediction 🫀</p>', unsafe_allow_html=True)


# Custom CSS
st.markdown("""
    <style>
    .custom-title {
        color: #FF6347;
        font-size: 36px;
    }
    .css-1d391kg {  # Set the width of the sidebar
        width: 300px;
    }
    .css-18e3th9 { # Set the margin of the sidebar
        margin-left: 310px;
    }
    .stSlider > div > div > div > div { # Set the background color of the slider
        background-color: #FF6347;
        font-size: 40px;
    }
    .css-145kmo2 { # Set font size of the text
        font-size: 40px;
    }
    p {
        font-size: 20px; # Set the font size of the text
    }
    </style>
        """, unsafe_allow_html=True)


# Sidebar for inputs
st.sidebar.title("Input your details below")
age = st.sidebar.number_input("Age", min_value=0, max_value=100, value=63)
sex = st.sidebar.select_slider("Sex (0 = female, 1 = male)", [0, 1], value=1)
cp = st.sidebar.select_slider("Chest pain type (range 1-4)", [1, 2, 3,4], value=3)
trestbps = st.sidebar.number_input("Resting blood pressure (mm Hg)", min_value=20, max_value=300, value=145)
thalach = st.sidebar.number_input("Maximum heart rate achieved", min_value=0, max_value=200, value=150)
chol = st.sidebar.number_input("Serum cholesterol in mg/dl", min_value=0, max_value=500, value=233)
fbs= st.sidebar.select_slider("Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)", [0, 1], value=1)
restecg = st.sidebar.select_slider("Resting electrocardiographic results (0-2)", [0, 1, 2], value=0)
exang = st.sidebar.select_slider("Exercise induced angina (1 = yes; 0 = no)", [0, 1],value=0)
oldpeak = st.sidebar.number_input("Depression induced by exercise relative to rest", min_value=0.0, max_value=10.0, value=2.3)
slope = st.sidebar.select_slider("Slope of peak exercise ST segment", [0, 1, 2],value=0)
ca = st.sidebar.select_slider("Number of major vessels (0-3) colored by fluoroscopy", [0, 1, 2, 3],value=0)
thal = st.sidebar.select_slider("Thalassemia", [0, 1, 2, 3],value=1)

# Calculate thalach_age_ratio and trestbps_age_ratio
if age>0:
    thalach_age_ratio = thalach/age
    trestbps_age_ratio = trestbps/age
    chol_age_ratio = chol/age
else:
    thalach_age_ratio = 0
    trestbps_age_ratio = 0
    chol_age_ratio = 0

# Create a submit button
st.sidebar.markdown("---")
submit_button = st.sidebar.button(label='Predict')


# Handle form submission
if submit_button:

    # Create Pandas DataFrame
    user_input = pd.DataFrame(
        data=[[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, thalach_age_ratio, trestbps_age_ratio, chol_age_ratio]],
        columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'thalach_age_ratio', 'trestbps_age_ratio', 'chol_age_ratio']
    )

    # Make the prediction
    prediction = final_pipeline.predict(user_input)

    # Display the prediction
    if prediction[0] == 0:
        st.subheader("**Prediction:** LOW probability of heart disease.")
    else:
        st.subheader("**Prediction:** **HIGH** probability of heart disease.")

    st.write(" ")
    st.write("---")
    st.write("**Disclaimer:** This prediction is based on a machine learning model with an accuracy rate of approximately 86%. It is important to consult with a healthcare professional for a comprehensive evaluation and diagnosis. The model's predictions should not be used as a substitute for professional medical advice or treatment.")

    st.image('images/features_correlation.png', caption='Correlation between Heart Disease and Features', use_column_width=True)

    st.image('images/final_pipeline.png', caption='Model pipeline used for this prediction', use_column_width=True)
