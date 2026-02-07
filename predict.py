# predict.py

import joblib
import random

# Load only the threshold
threshold = joblib.load("churn_threshold.pkl")

def predict_churn(input_data: dict):
    """
    Mock prediction function using only threshold.
    Returns a random probability for demonstration.
    """
    # Generate a pseudo probability (0.2 to 0.9) just for demo
    churn_prob = random.uniform(0.2, 0.9)

    return {
        "churn_probability": round(churn_prob, 3),
        "risk": "High" if churn_prob >= threshold else "Low"
    }
