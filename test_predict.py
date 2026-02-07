from predict import predict_churn

sample_input = {
    "gender": "Male",
    "Partner": "Yes",
    "tenure": 12,
    "MonthlyCharges": 70,
    "Contract": "Month-to-month",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "TechSupport": "No"
}

result = predict_churn(sample_input)
print(result)
