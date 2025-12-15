import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data
data = pd.read_csv("data/sample_training_data.csv")

X = data[["glucose", "hemoglobin", "cholesterol"]]
y = data["risk"]

# Train model
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

# Save model
with open("model/risk_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("ML model trained and saved successfully")
