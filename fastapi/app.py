import streamlit as st
import requests
import json

# Set page configuration
st.set_page_config(page_title="Health Assistant 🏥",
                   layout="wide",
                   page_icon="🧑‍⚕️")

API_URL = "http://127.0.0.1:5000"  # Change this if running on a different server

# Sidebar for navigation
with st.sidebar:
    selected = st.radio('Multiple Disease Prediction System 🏥',
                        ['Diabetes Predictions 🍩',
                         'Heart Disease Predictions ❤️',
                         "Parkinson's Predictions 🧠"])

# Diabetes Prediction Page 🍩
if selected == 'Diabetes Predictions 🍩':
    st.title('Diabetes Prediction using ML 🍬')

    col1, col2, col3 = st.columns(3)

    with col1: Pregnancies = st.text_input('Number of Pregnancies 🤰')
    with col2: Glucose = st.text_input('Glucose Level 💉')
    with col3: BloodPressure = st.text_input('Blood Pressure value 🩺')
    with col1: SkinThickness = st.text_input('Skin Thickness value 💪')
    with col2: Insulin = st.text_input('Insulin Level 💉')
    with col3: BMI = st.text_input('BMI value ⚖️')
    with col1: DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function 👨‍⚕️')
    with col2: Age = st.text_input('Age of the Person 🎂')

    if st.button('Diabetes Test Result 🩺'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]

        response = requests.post(f"{API_URL}/predict/diabetes", json={"features": user_input})
        prediction = response.json()['prediction']

        result = "The person is diabetic 🍩" if prediction == 1 else "The person is not diabetic 🍃"
        st.success(result)

# Heart Disease Prediction Page ❤️
if selected == 'Heart Disease Predictions ❤️':
    st.title('Heart Disease Prediction using ML ❤️')

    col1, col2, col3 = st.columns(3)

    with col1: age = st.text_input('Age 👶')
    with col2: sex = st.text_input('Sex 👨‍⚕️')
    with col3: cp = st.text_input('Chest Pain types ❤️')
    with col1: trestbps = st.text_input('Resting Blood Pressure 🩸')
    with col2: chol = st.text_input('Serum Cholestoral mg/dl 🧪')
    with col3: fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl 🍽️')
    with col1: restecg = st.text_input('Resting ECG results 🩺')
    with col2: thalach = st.text_input('Maximum Heart Rate ❤️')
    with col3: exang = st.text_input('Exercise Induced Angina 💪')
    with col1: oldpeak = st.text_input('ST depression induced by exercise 💪')
    with col2: slope = st.text_input('Slope of peak exercise ST segment 🏃')
    with col3: ca = st.text_input('Major vessels colored by fluoroscopy 🏥')
    with col1: thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect ⛔')

    if st.button('Heart Disease Test Result ❤️'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]

        response = requests.post(f"{API_URL}/predict/heart", json={"features": user_input})
        prediction = response.json()['prediction']

        result = "The person has heart disease ❤️" if prediction == 1 else "The person does not have heart disease 🍃"
        st.success(result)

# Parkinson's Prediction Page 🧠
if selected == "Parkinson's Predictions 🧠":
    st.title("Parkinson's Disease Prediction using ML 🧠")

    inputs = [st.text_input(label) for label in [
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
        'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 
        'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 
        'DFA', 'spread1', 'spread2', 'D2', 'PPE'
    ]]

    if st.button("Parkinson's Test Result 🧠"):
        user_input = [float(x) for x in inputs]

        response = requests.post(f"{API_URL}/predict/parkinsons", json={"features": user_input})
        prediction = response.json()['prediction']

        result = "The person has Parkinson's disease 🧠" if prediction == 1 else "The person does not have Parkinson's 🍀"
        st.success(result)
import streamlit as st
import requests
import json

# Set page configuration
st.set_page_config(page_title="Health Assistant 🏥",
                   layout="wide",
                   page_icon="🧑‍⚕️")

API_URL = "http://127.0.0.1:5000"  # Change this if running on a different server

# Sidebar for navigation
with st.sidebar:
    selected = st.radio('Multiple Disease Prediction System 🏥',
                        ['Diabetes Predictions 🍩',
                         'Heart Disease Predictions ❤️',
                         "Parkinson's Predictions 🧠"])

# Diabetes Prediction Page 🍩
if selected == 'Diabetes Predictions 🍩':
    st.title('Diabetes Prediction using ML 🍬')

    col1, col2, col3 = st.columns(3)

    with col1: Pregnancies = st.text_input('Number of Pregnancies 🤰')
    with col2: Glucose = st.text_input('Glucose Level 💉')
    with col3: BloodPressure = st.text_input('Blood Pressure value 🩺')
    with col1: SkinThickness = st.text_input('Skin Thickness value 💪')
    with col2: Insulin = st.text_input('Insulin Level 💉')
    with col3: BMI = st.text_input('BMI value ⚖️')
    with col1: DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function 👨‍⚕️')
    with col2: Age = st.text_input('Age of the Person 🎂')

    if st.button('Diabetes Test Result 🩺'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]

        response = requests.post(f"{API_URL}/predict/diabetes", json={"features": user_input})
        prediction = response.json()['prediction']

        result = "The person is diabetic 🍩" if prediction == 1 else "The person is not diabetic 🍃"
        st.success(result)

# Heart Disease Prediction Page ❤️
if selected == 'Heart Disease Predictions ❤️':
    st.title('Heart Disease Prediction using ML ❤️')

    col1, col2, col3 = st.columns(3)

    with col1: age = st.text_input('Age 👶')
    with col2: sex = st.text_input('Sex 👨‍⚕️')
    with col3: cp = st.text_input('Chest Pain types ❤️')
    with col1: trestbps = st.text_input('Resting Blood Pressure 🩸')
    with col2: chol = st.text_input('Serum Cholestoral mg/dl 🧪')
    with col3: fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl 🍽️')
    with col1: restecg = st.text_input('Resting ECG results 🩺')
    with col2: thalach = st.text_input('Maximum Heart Rate ❤️')
    with col3: exang = st.text_input('Exercise Induced Angina 💪')
    with col1: oldpeak = st.text_input('ST depression induced by exercise 💪')
    with col2: slope = st.text_input('Slope of peak exercise ST segment 🏃')
    with col3: ca = st.text_input('Major vessels colored by fluoroscopy 🏥')
    with col1: thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect ⛔')

    if st.button('Heart Disease Test Result ❤️'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]

        response = requests.post(f"{API_URL}/predict/heart", json={"features": user_input})
        prediction = response.json()['prediction']

        result = "The person has heart disease ❤️" if prediction == 1 else "The person does not have heart disease 🍃"
        st.success(result)

# Parkinson's Prediction Page 🧠
if selected == "Parkinson's Predictions 🧠":
    st.title("Parkinson's Disease Prediction using ML 🧠")

    inputs = [st.text_input(label) for label in [
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
        'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 
        'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 
        'DFA', 'spread1', 'spread2', 'D2', 'PPE'
    ]]

    if st.button("Parkinson's Test Result 🧠"):
        user_input = [float(x) for x in inputs]

        response = requests.post(f"{API_URL}/predict/parkinsons", json={"features": user_input})
        prediction = response.json()['prediction']

        result = "The person has Parkinson's disease 🧠" if prediction == 1 else "The person does not have Parkinson's 🍀"
        st.success(result)
