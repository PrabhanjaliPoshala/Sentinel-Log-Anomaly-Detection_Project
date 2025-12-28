import pickle
import yaml
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import IsolationForest

# Load configuration
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Load logs
with open("sample.log", "r") as f:
    logs = [line.strip() for line in f if line.strip()]

# Vectorization
vectorizer = TfidfVectorizer(max_features=100)
X = vectorizer.fit_transform(logs)

# Train model
model = IsolationForest(
    contamination=config["anomaly_threshold"],
    random_state=42
)
model.fit(X)

# Save model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and TF-IDF vectorizer trained and saved")
