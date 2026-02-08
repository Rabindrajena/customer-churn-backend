# predict.py
import joblib
import pandas as pd
import os

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "churn_model.pkl")
THRESHOLD_PATH = os.path.join(BASE_DIR, "churn_threshold.pkl")

# Load model & threshold
model = joblib.load(MODEL_PATH)
threshold = joblib.load(THRESHOLD_PATH)

# List of all features the model expects
REQUIRED_COLUMNS = [
    'gender', 'Partner', 'tenure', 'MonthlyCharges', 'Contract', 'InternetService',
    'OnlineSecurity', 'TechSupport', 'PhoneService', 'StreamingMovies', 'Dependents',
    'StreamingTV', 'PaymentMethod', 'DeviceProtection', 'OnlineBackup', 'MultipleLines',
    'SeniorCitizen', 'TotalCharges', 'PaperlessBilling'
]

def predict_churn(input_data: dict):
    """
    Predict churn probability using trained ML model
    and apply custom threshold. Automatically fills missing columns.
    """

    # Convert input to DataFrame
    input_df = pd.DataFrame([input_data])

    # Drop ID if accidentally passed
    if "customerID" in input_df.columns:
        input_df.drop(columns=["customerID"], inplace=True)

    # Fill missing columns with default values
    for col in REQUIRED_COLUMNS:
        if col not in input_df.columns:
            # Numeric columns
            if col in ['tenure', 'MonthlyCharges', 'SeniorCitizen', 'TotalCharges']:
                input_df[col] = 0
            # Categorical/string columns
            else:
                input_df[col] = 'No'

    # Reorder columns to match model (optional but safe)
    input_df = input_df[REQUIRED_COLUMNS]

    # Predict probability
    churn_proba = model.predict_proba(input_df)[0][1]

    # Risk logic
    if churn_proba >= threshold:
        risk = "High"
    elif churn_proba >= 0.2:
        risk = "Moderate"
    else:
        risk = "Low"

    return {
        "churn_probability": round(float(churn_proba), 3),
        "risk": risk
    }
