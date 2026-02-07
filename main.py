from fastapi import FastAPI
from predict import predict_churn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ASGI app must be named 'app'
app = FastAPI(title="Customer Churn Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
def predict_endpoint(data: CustomerInput):
    return predict_churn(data.dict())
