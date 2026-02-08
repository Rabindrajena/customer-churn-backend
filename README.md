# Customer Churn Prediction Backend

This is the **backend API** for predicting customer churn using a trained machine learning model. It is built with **FastAPI** and deployed on **Render**.

---

## Features

- Accepts customer data via a REST API (`/predict`)  
- Returns churn probability and risk category (Low / Moderate / High)  
- Handles missing fields automatically for robustness  
- Supports cross-origin requests for frontend integration (CORS enabled)

---

## Endpoints

### **GET /**

Check if the API is running.

```http
GET /
```

**Response:**

```json
{
  "status": "API is running"
}
```
---

### **POST /predict**

Predict customer churn.

```http
POST /predict
Content-Type: application/json
```
**Request Body Example:**

```json
{
  "gender": "Male",
  "Partner": "Yes",
  "tenure": 12,
  "MonthlyCharges": 70,
  "Contract": "Month-to-month",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "TechSupport": "Yes"
}
```

**Response Example:**

```json
{
  "churn_probability": 0.511,
  "risk": "High"
}
```
---

### **Installation & Setup** (Local)

 **1.** Clone the repository:

```bash
git clone https://github.com/Rabindrajena/customer-churn-backend.git
cd customer-churn-backend
```

**2.** Install dependencies:

```bash
pip install -r requirements.txt
```

**3.** Run the API locally:

```bash
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000/.

---

### **Deployment**

* Deployed on **Render**: [https://customer-churn-backend-7hly.onrender.com]

* Python runtime: 3.11

* Procfile: web: uvicorn main:app --host 0.0.0.0 --port $PORT

---

### **Files**

* `main.py` → FastAPI app

* `predict.py` → Prediction logic

* `churn_model.pkl` → Trained ML model

* `churn_threshold.pkl` → Threshold for risk categories

* `requirements.txt` → Python dependencies

* `Procfile & runtime.txt` → Deployment configuration

---

### **Notes**

* Ensure all required fields are sent in the POST request. Missing optional fields are automatically handled.

* Designed to be **integrated with a frontend** (React, Vue, or any other).
