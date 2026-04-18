import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('student_performance_model.pkl')

# Streamlit App Title
st.title("Student Performance Prediction")

st.write("""
### Predict Grades Based on Input Factors
Enter the details below to predict a student's performance.
""")

# Sidebar for input
st.sidebar.header("Input Features")

def user_input_features():
    socioeconomic_score = st.sidebar.slider("Socioeconomic Score", 0.0, 1.0, 0.5)
    study_hours = st.sidebar.slider("Study Hours", 0.0, 10.0, 5.0)
    sleep_hours = st.sidebar.slider("Sleep Hours", 0.0, 12.0, 7.0)
    attendance = st.sidebar.slider("Attendance (%)", 0.0, 100.0, 75.0)
    performance_medium = st.sidebar.selectbox("Performance (Medium)", [0, 1], index=0)
    performance_high = st.sidebar.selectbox("Performance (High)", [0, 1], index=0)
    
    # Create a dataframe for input features
    data = {
        'Socioeconomic Score': socioeconomic_score,
        'Study Hours': study_hours,
        'Sleep Hours': sleep_hours,
        'Attendance (%)': attendance,
        'Performance_Medium': performance_medium,
        'Performance_High': performance_high
    }
    return pd.DataFrame(data, index=[0])

# Get user input
input_data = user_input_features()

# Display user input
st.subheader("User Input Features")
st.write(input_data)

# Predict grades using the model
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.subheader("Predicted Grade")
    st.write(f"Estimated Grade: {prediction[0]:.2f}")

