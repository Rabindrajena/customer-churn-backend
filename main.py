# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from predict import predict_churn

app = FastAPI(title="Customer Churn Prediction API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all frontend origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CustomerInput(BaseModel):
    gender: str
    Partner: str
    tenure: int
    MonthlyCharges: float
    Contract: str
    InternetService: str
    OnlineSecurity: str
    TechSupport: str

@app.get("/")
def home():
    return {"status": "API is running"}

@app.post("/predict")
def predict(data: CustomerInput):
    return predict_churn(data.dict())
