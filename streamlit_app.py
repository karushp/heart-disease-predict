import sys
import os
import streamlit as st
import numpy as np

from data_prep import scaler
from model_train import model, accuracy

# Title for the Streamlit app
st.title("Probability of Heart Disease")

st.markdown("""
    <style>
    .full-width-form {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

'''
# Create two columns
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=0, max_value=100, value=0)
    sex = st.selectbox("Sex (0 = female, 1 = male)", [0, 1])
    cp = st.selectbox("Chest pain type (range 1-4)", [1, 2, 3,4])
    trestbps = st.number_input("Resting blood pressure (mm Hg)", min_value=20, max_value=300, value=20)

with col2:
    chol = st.number_input("Cholesterol(mg/dl)", min_value=0, max_value=600, value=0)
    fbs = st.selectbox("Fasting blood sugar(> 120 mg/dl [1 = true; 0 = false])", [0, 1])
    restecg = st.selectbox("Resting electrocardiographic results", [0, 1, 2])
    thalach = st.number_input("Maximum heart rate achieved", min_value=0, max_value=200, value=0)

with col3:
    exang = st.selectbox("Exercise induced angina (1 = yes; 0 = no)", [0, 1])
    oldpeak = st.number_input("ST depression induced by exercise relative to rest", min_value=0.0, max_value=10.0, value=0.0)
    slope = st.selectbox("Slope of peak exercise ST segment", [0, 1, 2])
    ca = st.selectbox("Number of major vessels (0-3) colored by fluoroscopy", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia", [0, 1, 2, 3])



with st.form(' Heart Disease Prediction'):

    age = st.number_input("Age", min_value=0, max_value=100, value=0)
    sex = st.select_slider("Sex (0 = female, 1 = male)", [0, 1])
    cp = st.select_slider("Chest pain type (range 1-4)", [1, 2, 3,4])
    trestbps = st.slider("Resting blood pressure (mm Hg)", min_value=20, max_value=300, value=20)
    thalch = st.slider("Maximum heart rate achieved", min_value=0, max_value=200, value=0)
    exang = st.select_slider("Exercise induced angina (1 = yes; 0 = no)", [0, 1])
    oldpeak = st.slider("ST depression induced by exercise relative to rest", min_value=0.0, max_value=10.0, value=0.0)
    slope = st.select_slider("Slope of peak exercise ST segment", [0, 1, 2])
    ca = st.select_slider("Number of major vessels (0-3) colored by fluoroscopy", [0, 1, 2, 3])
    thal = st.select_slider("Thalassemia", [0, 1, 2, 3])

    submit_button = st.form_submit_button(label='Predict')
'''

# Create a form
with st.form(key='heart_disease_form'):
    # Initialize session state for each feature
    if 'sex' not in st.session_state:
        st.session_state.sex = 0
    if 'cp' not in st.session_state:
        st.session_state.cp = 1
    if 'exang' not in st.session_state:
        st.session_state.exang = 0
    if 'slope' not in st.session_state:
        st.session_state.slope = 0
    if 'ca' not in st.session_state:
        st.session_state.ca = 0
    if 'thal' not in st.session_state:
        st.session_state.thal = 0

    # Number input for age
    age = st.number_input("Age", min_value=0, max_value=100, value=0)

    # Buttons for Sex (0 = female, 1 = male)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sex: Female", key='sex_female'):
            st.session_state.sex = 0
    with col2:
        if st.button("Sex: Male", key='sex_male'):
            st.session_state.sex = 1

    # Buttons for Chest pain type (range 1-4)
    col1, col2, col3, col4 = st.columns(4)
    for i in range(1, 5):
        with st.columns(4)[i-1]:
            if st.button(f"CP: {i}", key=f'cp_{i}'):
                st.session_state.cp = i

    # Slider for Resting blood pressure (mm Hg)
    trestbps = st.slider("Resting blood pressure (mm Hg)", min_value=20, max_value=300, value=20)

    # Slider for Maximum heart rate achieved
    thalch = st.slider("Maximum heart rate achieved", min_value=0, max_value=200, value=0)

    # Buttons for Exercise induced angina (1 = yes; 0 = no)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Exang: No", key='exang_no'):
            st.session_state.exang = 0
    with col2:
        if st.button("Exang: Yes", key='exang_yes'):
            st.session_state.exang = 1

    # Slider for ST depression induced by exercise relative to rest
    oldpeak = st.slider("ST depression induced by exercise relative to rest", min_value=0.0, max_value=10.0, value=0.0)

    # Buttons for Slope of peak exercise ST segment
    col1, col2, col3 = st.columns(3)
    for i in range(3):
        with st.columns(3)[i]:
            if st.button(f"Slope: {i}", key=f'slope_{i}'):
                st.session_state.slope = i

    # Buttons for Number of major vessels (0-3) colored by fluoroscopy
    col1, col2, col3, col4 = st.columns(4)
    for i in range(4):
        with st.columns(4)[i]:
            if st.button(f"CA: {i}", key=f'ca_{i}'):
                st.session_state.ca = i

    # Buttons for Thalassemia
    col1, col2, col3, col4 = st.columns(4)
    for i in range(4):
        with st.columns(4)[i]:
            if st.button(f"Thal: {i}", key=f'thal_{i}'):
                st.session_state.thal = i

    # Submit button for the form
    submit_button = st.form_submit_button(label='Submit')

    # Display the results when the form is submitted
    if submit_button:
        st.write(f"Age: {age}")
        st.write(f"Sex: {st.session_state.sex}")
        st.write(f"Chest Pain Type: {st.session_state.cp}")
        st.write(f"Resting Blood Pressure: {trestbps}")
        st.write(f"Maximum Heart Rate Achieved: {thalch}")
        st.write(f"Exercise Induced Angina: {st.session_state.exang}")
        st.write(f"ST Depression Induced by Exercise Relative to Rest: {oldpeak}")
        st.write(f"Slope of Peak Exercise ST Segment: {st.session_state.slope}")
        st.write(f"Number of Major Vessels Colored by Fluoroscopy: {st.session_state.ca}")
        st.write(f"Thalassemia: {st.session_state.thal}")


'''
# Create a button to trigger the prediction
if st.button("Predict"):
    # Create a list of the user input
    user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    # Convert the list to a numpy array
    user_input = np.array(user_input).reshape(1, -1)
    user_data_scaled = scaler.fit_transform(user_input)


    # Make the prediction
    prediction = model.predict(user_data_scaled)

    # Display the prediction
    if prediction[0] == 0:
        st.write("There is low probability of a heart disease.")
    else:
        st.write("There is high probability that person has a heart. Please consult your doctor urgently.")

    st.write(f'Model Accuracy: {accuracy:.2f}')

'''
