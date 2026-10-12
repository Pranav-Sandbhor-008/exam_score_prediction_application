# 🎓 Student Performance & Score Predictor

A Machine Learning web application that predicts a student's estimated academic performance score based on study habits, sleep patterns, attendance, and other academic and lifestyle factors.

The application uses a **K-Nearest Neighbors (KNN) Regression model** and an interactive **Streamlit** interface to make score prediction simple and accessible.

## 🚀 Live Demo

**Try the application here:**  
👉 https://examscorepredictionapplication-ctqyym9iwuvmjplcbjsbej.streamlit.app/

## ✨ Features

- 🎯 **Score Prediction:** Estimates student performance using a trained KNN regression model.
- 👤 **Student Information:** Enter age and gender.
- 📚 **Study Habits:** Specify daily study hours and study method.
- 😴 **Sleep Analysis:** Include sleep duration and sleep quality.
- 🏫 **Academic Factors:** Consider course stream, class attendance, and exam difficulty.
- 🌐 **Learning Resources:** Include internet access and facility ratings.
- 🖥️ **Interactive Interface:** User-friendly web application built with Streamlit.
- ⚡ **Instant Results:** Generate an estimated performance score from the submitted parameters.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **ML Algorithm:** K-Nearest Neighbors (KNN) Regression
- **Web Framework:** Streamlit
- **Model Storage:** Pickle (`.pkl`)

## 📂 Project Structure

```text
exam_score_prediction_application/
│
├── app.py          # Streamlit application
├── knn.pkl         # Trained KNN regression model
├── requirements.txt # Python dependencies
├── README.md       # Project documentation
└── .gitignore      # Git ignored files (if configured)
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Pranav-Sandbhor-008/exam_score_prediction_application.git
```

### 2. Navigate to the Project Directory

```bash
cd exam_score_prediction_application
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment.

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

The application will start locally. Open the URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 🧠 How It Works

1. The user enters student information and study-related parameters.
2. The application processes the inputs in the format expected by the trained model.
3. The trained KNN regression model (`knn.pkl`) generates a score prediction.
4. The application displays the estimated performance score in the Streamlit interface.

### Model Overview

**K-Nearest Neighbors Regression (KNN)** predicts a numerical value by identifying similar observations in the training data and estimating the target value from their outcomes.

The quality of predictions depends on the training dataset, feature preprocessing, and model evaluation.

## 🎯 Project Objectives

- Apply machine learning regression techniques to an educational use case.
- Explore the relationship between study habits and estimated academic performance.
- Build an interactive interface for model predictions.
- Deploy a machine learning application for public access.
- Strengthen practical skills in Python, machine learning, and web application development.

## 🔮 Future Improvements

- 📊 Add data visualizations to explore study habits and performance.
- 📈 Display feature importance or other model interpretation insights where appropriate.
- 🧪 Include model evaluation metrics such as MAE, MSE, and R².
- 📋 Provide personalized study recommendations.
- 📱 Improve mobile responsiveness and accessibility.
- 🔄 Compare KNN with other regression algorithms.

## 👨‍💻 Author

**Pranav Sandbhor**

- **GitHub:** https://github.com/Pranav-Sandbhor-008
- **Project Repository:** https://github.com/Pranav-Sandbhor-008/exam_score_prediction_application
- **Live Application:** https://examscorepredictionapplication-ctqyym9iwuvmjplcbjsbej.streamlit.app/

---

⭐ If you find this project interesting, consider giving the repository a star!

💬 Suggestions and contributions are welcome.
