
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib

data = {
    "crowd": np.random.randint(30, 100, 500),
    "waste": np.random.randint(40, 100, 500),
    "runtime": np.random.randint(100, 500, 500)
}

df = pd.DataFrame(data)
df["risk"] = ((df["crowd"] > 80) | (df["waste"] > 85)).astype(int)

model = LogisticRegression()
model.fit(df[["crowd", "waste", "runtime"]], df["risk"])

joblib.dump(model, "backend/app/models/risk_model.pkl")
print("Model trained and saved.")
