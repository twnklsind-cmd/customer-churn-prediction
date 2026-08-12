# Customer Churn Prediction

A machine learning web app that predicts whether a telecom customer will churn (leave the service), built as part of my Data Science portfolio.

## Problem Statement

Telecom companies lose millions every year to customer churn. This project builds a model to identify at-risk customers early so the business can take action.

## Dataset

- **Source:** Telco Customer Churn — IBM / Kaggle
- **Size:** 7,043 customers, 21 features
- **Target:** Churn (Yes/No)

## Tech Stack

- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **App:** Streamlit
- **Model:** Random Forest Classifier

## What I Did

- Performed Exploratory Data Analysis (EDA) to find churn patterns
- Preprocessed data — handled missing values, encoded categoricals, scaled features
- Trained and compared Logistic Regression vs Random Forest
- Built an interactive web app for real-time predictions

## Results

| Model               | Accuracy | ROC-AUC |
| ------------------- | -------- | ------- |
| Logistic Regression | ~80%     | ~83%    |
| Random Forest       | ~80%     | ~84%    |

## Key Findings

- Month-to-month contract customers churn the most
- Higher monthly charges = higher churn risk
- Longer tenure customers are more likely to stay
- Fiber optic internet customers churn more than DSL

## How to Run Locally

# Clone the repo

git clone https://github.com/yourusername/customer-churn-prediction

# Install dependencies

pip install -r requirements.txt

# Run the app

streamlit run app.py

```

##  Project Structure
```

customer-churn-prediction/
├── data/
│ └── churn.csv
├── models/
│ ├── churn_model.pkl
│ └── scaler.pkl
├── notebooks/
│ └── churn_analysis.ipynb
├── app.py
├── requirements.txt
└── README.md

```

```
