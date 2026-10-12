import pickle
import numpy as np
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for Modern Shadows, Cards, and Layout
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff2b2b;
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    .prediction-card {
        background-color: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        text-align: center;
        margin-top: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Load the trained KNN Regressor model
@st.cache_resource
def load_model():
  try:
    with open("knn.pkl", "rb") as file:
      model = pickle.load(file)
    return model
  except FileNotFoundError:
    return None


model = load_model()

# Header Section
st.title("🎓 Student Performance & Score Predictor")
st.markdown(
    "Enter the student's study habits and parameters below to estimate their"
    " academic performance using your trained **K-Nearest Neighbors (KNN)**"
    " regression model."
)
st.markdown("---")

if model is None:
  st.error(
      "⚠️ Model file `knn.pkl` not found in the directory. Please make sure"
      " `knn.pkl` is in the same folder as `app.py`."
  )
else:
  with st.form("prediction_form"):
    st.markdown("### 📝 Enter Student Parameters")

    col1, col2 = st.columns(2)

    with col1:
      age = st.number_input("Age", min_value=10, max_value=50, value=20, step=1)
      gender = st.selectbox("Gender", ["Female", "Male"])
      course = st.selectbox(
          "Course / Stream",
          ["Science", "Commerce", "Arts", "Engineering", "Other"],
      )
      study_hours = st.slider(
          "Daily Study Hours", min_value=0.0, max_value=16.0, value=4.0, step=0.5
      )
      class_attendance = st.slider(
          "Class Attendance (%)",
          min_value=0.0,
          max_value=100.0,
          value=75.0,
          step=1.0,
      )
      internet_access = st.selectbox("Internet Access", ["Yes", "No"])

    with col2:
      sleep_hours = st.slider(
          "Sleep Hours per Night", min_value=2.0, max_value=12.0, value=7.0, step=0.5
      )
      sleep_quality = st.selectbox(
          "Sleep Quality", ["Poor", "Average", "Good", "Excellent"]
      )
      study_method = st.selectbox(
          "Study Method",
          ["Self Study", "Online Classes", "Group Study", "Coaching"],
      )
      facility_rating = st.slider(
          "Facility Rating (1-5)", min_value=1, max_value=5, value=3, step=1
      )
      exam_difficulty = st.selectbox(
          "Exam Difficulty", ["Easy", "Moderate", "Hard"]
      )

    st.markdown("<br>", unsafe_allow_html=True)
    submit_button = st.form_submit_button(label="Predict Score")

  if submit_button:
    # Encoding mappings matching standard categorical preprocessing
    gender_enc = 1 if gender == "Male" else 0
    internet_enc = 1 if internet_access == "Yes" else 0

    course_mapping = {
        "Science": 0,
        "Commerce": 1,
        "Arts": 2,
        "Engineering": 3,
        "Other": 4,
    }
    sleep_quality_mapping = {"Poor": 0, "Average": 1, "Good": 2, "Excellent": 3}
    study_method_mapping = {
        "Self Study": 0,
        "Online Classes": 1,
        "Group Study": 2,
        "Coaching": 3,
    }
    exam_difficulty_mapping = {"Easy": 0, "Moderate": 1, "Hard": 2}

    # Construct feature vector corresponding to trained model input columns:
    # ['age', 'gender', 'course', 'study_hours', 'class_attendance', 'internet_access',
    #  'sleep_hours', 'sleep_quality', 'study_method', 'facility_rating', 'exam_difficulty']
    features = np.array([[
        age,
        gender_enc,
        course_mapping.get(course, 0),
        study_hours,
        class_attendance,
        internet_enc,
        sleep_hours,
        sleep_quality_mapping.get(sleep_quality, 1),
        study_method_mapping.get(study_method, 0),
        facility_rating,
        exam_difficulty_mapping.get(exam_difficulty, 1),
    ]])

    try:
      prediction = model.predict(features)[0]
      st.markdown(
          f"""
            <div class="prediction-card">
                <h4 style="color: #31333F; margin-bottom: 0.5rem;">Estimated Performance Score</h4>
                <h1 style="color: #ff4b4b; font-size: 3rem; margin: 0;">{prediction:.2f}</h1>
                <p style="color: gray; margin-top: 0.5rem;">Generated using KNeighborsRegressor model.</p>
            </div>
            """,
          unsafe_allow_html=True,
      )
    except Exception as e:
      st.error(f"Error generating prediction: {e}")
