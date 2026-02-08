# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from predict import predict_churn

app = FastAPI(title="Customer Churn Prediction API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from predict import predict_churn
import traceback  # <-- import traceback here

app = FastAPI(title="Customer Churn Prediction API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model
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

# -----------------------------
# Updated /predict endpoint
@app.post("/predict")
def predict_endpoint(data: CustomerInput):
    try:
        result = predict_churn(data.dict())
        return result
    except Exception as e:
        # Print full traceback to Render logs
        traceback.print_exc()
        # Return readable error to client
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
# -----------------------------

# Pydantic model for request validation
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
    try:
        # Call the predict function
        result = predict_churn(data.dict())
        return result
    except Exception as e:
        # Return error details for debugging (optional: remove in production)
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
