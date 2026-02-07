# predict.py
import joblib
import pandas as pd

MODEL_PATH = "churn_model.pkl"
THRESHOLD_PATH = "churn_threshold.pkl"

# Load model & threshold
model = joblib.load(MODEL_PATH)
threshold = joblib.load(THRESHOLD_PATH)

def predict_churn(input_data: dict):
    """
    Predict churn probability using trained ML model
    and apply custom threshold.
    """

    # Convert input to DataFrame
    input_df = pd.DataFrame([input_data])

    # Drop ID if accidentally passed
    if "customerID" in input_df.columns:
        input_df.drop(columns=["customerID"], inplace=True)

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
