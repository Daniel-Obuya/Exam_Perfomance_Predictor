import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('gb_model_reduced.pkl', 'rb'))

# Define the feature list (copy from your notebook)
high_importance_features = [
    'Hours_Studied',
    'Attendance',
    'Parental_Involvement',
    'Access_to_Resources',
    'Extracurricular_Activities',
    'Sleep_Hours',
    'Previous_Scores',
    'Motivation_Level',
    'Internet_Access',
    'Tutoring_Sessions',
    'Family_Income',
    'Teacher_Quality',
    'Peer_Influence',
    'Physical_Activity',
    'Learning_Disabilities',
    'Parental_Education_Level',
    'Distance_from_Home'
]

st.title("Student Performance Prediction")

# Input form for all features
input_data = {}
input_data['Hours_Studied'] = st.number_input('Hours Studied', min_value=0)
input_data['Attendance'] = st.number_input('Attendance (%)', min_value=0, max_value=100)
input_data['Parental_Involvement'] = st.selectbox('Parental Involvement', [1, 2, 3], format_func=lambda x: {1:'Low',2:'Medium',3:'High'}[x])
input_data['Access_to_Resources'] = st.selectbox('Access to Resources', [1, 2, 3], format_func=lambda x: {1:'Low',2:'Medium',3:'High'}[x])
input_data['Extracurricular_Activities'] = st.selectbox('Extracurricular Activities', [0, 1], format_func=lambda x: {0:'No',1:'Yes'}[x])
input_data['Sleep_Hours'] = st.number_input('Sleep Hours', min_value=0)
input_data['Previous_Scores'] = st.number_input('Previous Scores', min_value=0)
input_data['Motivation_Level'] = st.selectbox('Motivation Level', [1, 2, 3], format_func=lambda x: {1:'Low',2:'Medium',3:'High'}[x])
input_data['Internet_Access'] = st.selectbox('Internet Access', [0, 1], format_func=lambda x: {0:'No',1:'Yes'}[x])
input_data['Tutoring_Sessions'] = st.number_input('Tutoring Sessions', min_value=0)
input_data['Family_Income'] = st.selectbox('Family Income', [1, 2, 3], format_func=lambda x: {1:'Low',2:'Medium',3:'High'}[x])
input_data['Teacher_Quality'] = st.selectbox('Teacher Quality', [1, 2, 3], format_func=lambda x: {1:'Low',2:'Medium',3:'High'}[x])
input_data['Peer_Influence'] = st.selectbox('Peer Influence', [1, 2, 3], format_func=lambda x: {1:'Negative',2:'Neutral',3:'Positive'}[x])
input_data['Physical_Activity'] = st.number_input('Physical Activity', min_value=0)
input_data['Learning_Disabilities'] = st.selectbox('Learning Disabilities', [0, 1], format_func=lambda x: {0:'No',1:'Yes'}[x])
input_data['Parental_Education_Level'] = st.selectbox('Parental Education Level', [1, 2, 3], format_func=lambda x: {1:'High School',2:'College',3:'Postgraduate'}[x])
input_data['Distance_from_Home'] = st.selectbox('Distance from Home', [1, 2, 3], format_func=lambda x: {1:'Near',2:'Moderate',3:'Far'}[x])

# Prediction
if st.button('Predict'):
    df = pd.DataFrame([input_data])
    df = df[high_importance_features]
    predicted_score = model.predict(df)[0]
    st.success(f'Predicted Exam Score: {predicted_score:.2f}')
    if predicted_score >= 40:
        st.info('You have passed the exam!')
    else:
        st.warning('Work harder! You have not reached the passmark.')