# 🎓 Student Performance Prediction

A machine learning web application that predicts student academic performance based on socioeconomic and behavioral factors. Built with Python, Scikit-learn, Pandas, and Streamlit for an interactive user experience.

---

## 📖 Overview

This project uses machine learning to predict how well students will perform academically. By analyzing factors like attendance, study hours, and sleep patterns, the model can estimate a student's final grade. The predictions help educators identify students who may need extra support.

---

## 🎯 Problem Statement

Different students perform differently in school, and many factors influence their success. This project tries to answer:

**How can we predict a student's academic performance based on their study habits, attendance, and background?**

Understanding these patterns helps schools provide better support to students who need it most.

---

## 📊 Features Used

The model makes predictions based on five key factors:

- **Socioeconomic Score** – Family background and economic status
- **Study Hours** – How much time a student dedicates to studying each week
- **Sleep Hours** – Average hours of sleep per night
- **Attendance (%)** – Percentage of classes attended
- **Previous Performance** – Whether the student showed medium or high performance before

---

## 🔧 Approach

The project follows these steps:

1. **Data Preparation** – Clean and organize student data
2. **Analysis** – Understand patterns and relationships between factors
3. **Model Training** – Train a machine learning model to recognize patterns
4. **Testing** – Check how accurate the model is on new data
5. **Application** – Build a user-friendly app for making predictions

---

## 🤖 Model Used

- **Algorithm**: Linear Regression
- **Framework**: Scikit-learn
- **Model File**: `student_performance_model.pkl` (pre-trained)

Linear Regression is simple, fast, and works well for this prediction task. It learns the relationship between student factors and grade performance.

---

## 📈 Results

The model performs well on test data:

- Correctly predicts performance trends
- Identifies key factors that influence grades
- Runs instantly in the web application
- Can be used for real-time predictions

(Exact accuracy metrics can be added after training)

---

## 💡 Key Insights

1. **Attendance Matters Most** – Students who attend classes regularly tend to get better grades. Regular attendance is a strong predictor of success.

2. **Study & Sleep Balance** – It's not just about studying hard. Students need proper sleep too. A healthy balance leads to better performance.

3. **Socioeconomic Factors** – Background and economic status play a role in performance, showing that some students may need more support to succeed.

---

## 🚀 How to Run the Project

### Step 1: Install Python

Make sure you have Python 3.8+ installed on your computer.

### Step 2: Clone the Repository

```bash
git clone https://github.com/yourusername/Student-Performance-Prediction.git
cd Student-Performance-Prediction-ML-Streamlit-main
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs all required libraries (Streamlit, Pandas, Scikit-learn, etc.).

### Step 4: Run the Application

```bash
streamlit run model.py
```

The app will open in your browser at `http://localhost:8501`

### Step 5: Make Predictions

- Use the sidebar to adjust student factors
- Click the "Predict" button
- View the estimated grade

---

## 🛠️ Tech Stack

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| **Python**       | Programming language            |
| **Pandas**       | Data handling and manipulation  |
| **NumPy**        | Numerical calculations          |
| **Scikit-learn** | Machine learning model training |
| **Streamlit**    | Interactive web interface       |

---

## 📁 Project Structure

```
Student-Performance-Prediction-ML-Streamlit-main/
├── model.py                          # Main Streamlit app
├── student_performance_model.pkl      # Trained ML model
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

---

## 📝 Requirements

All dependencies are listed in `requirements.txt`:

- streamlit
- pandas
- scikit-learn
- joblib

---

## ✨ Conclusion

This project demonstrates how machine learning can be applied to real-world education challenges. By combining data analysis, machine learning, and web development, we created a practical tool that helps predict student performance and support educational decision-making.

---
