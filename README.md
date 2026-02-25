# Titanic Survival Prediction
# Project Overview

The Titanic Survival Prediction project is a Machine Learning application that predicts whether a passenger would survive the Titanic disaster based on historical passenger data.

This project demonstrates a complete end-to-end Machine Learning workflow:

Data preprocessing

Feature engineering

Model training

Model evaluation

Model deployment using Streamlit

The trained model is deployed as an interactive web application.

# Dataset Information

The dataset used in this project is the Titanic dataset, which contains passenger details and survival outcomes.

# Features Used
# Feature	Description
Pclass	Passenger class (1 = First, 2 = Second, 3 = Third)
Sex	Gender of the passenger
Age	Age of the passenger
SibSp	Number of siblings/spouses aboard
Parch	Number of parents/children aboard
Fare	Ticket fare
Embarked	Port of embarkation (C, Q, S)
Survived	Target variable (0 = Did not survive, 1 = Survived)
Model Information

Model Type: Random Forest Classifier

Problem Type: Binary Classification

['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

## The trained model is saved as:

titanic_model.pkl

# Application Information

The project includes a Streamlit web application that allows users to:

Enter passenger details

Generate survival predictions

View prediction results instantly

The application includes a custom user interface with background styling and structured input layout.

## Installation and Setup
1. Clone the Repository
git clone <areebkhan-ds/titanic-survival-analysis>
cd Titanic-Survival-Analysis
2. Install Dependencies

If a requirements.txt file is available:

pip install -r requirements.txt

Or install manually:

pip install streamlit scikit-learn pandas numpy joblib
How to Run the Application

Open a terminal inside the project folder and run:

streamlit run app.py

After running the command, the application will open automatically in your browser at:

http://localhost:8501
Model Training

To retrain the model:

Open train_model.ipynb

Run all cells

The trained model will be saved as:

titanic_model.pkl

Evaluation Metric: Accuracy

Features Used:
