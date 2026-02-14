
import joblib

model = joblib.load("backend/models/risk_model.pkl")

def predict_risk(crowd, waste, runtime):
    result = model.predict([[crowd, waste, runtime]])
    return "High" if result[0] == 1 else "Low"
