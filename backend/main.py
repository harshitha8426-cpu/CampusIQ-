
from fastapi import FastAPI
from backend.services.simulator_services import generate_data
from backend.services.prediction_service import predict_risk

app = FastAPI(title="CampusIQ API")

@app.get("/")
def home():
    return {"message": "CampusIQ AI System Running"}

@app.get("/api/dashboard")
def dashboard():
    data = generate_data()
    risk = predict_risk(data["crowd"], data["waste"], data["runtime"])
    data["risk_level"] = risk
    return data
