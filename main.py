import pickle
import pandas as pd
import os

# Load model and threshold once when the app starts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "churn_model.pkl")
THRESHOLD_PATH = os.path.join(BASE_DIR, "churn_threshold.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(THRESHOLD_PATH, "rb") as f:
    threshold = pickle.load(f)

def predict_churn(data: dict) -> dict:
    """
    Predict churn probability and decision for a customer.
    
    Args:
        data (dict): Input features from CustomerInput Pydantic model

    Returns:
        dict: {"churn_probability": float, "churn": bool}
    """
    # Convert dict to DataFrame (1 row)
    df = pd.DataFrame([data])

    # Predict probability
    probability = model.predict_proba(df)[:, 1][0]  # assuming positive class is at index 1

    # Decide churn based on threshold
    churn = probability >= threshold

    return {
        "churn_probability": round(probability, 4),
        "churn": bool(churn)
    }
