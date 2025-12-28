import time
import pickle
from features import extract_features

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("🚀 Sentinel started monitoring logs...")

seen = set()

while True:
    with open("sample.log", "r") as f:
        lines = f.readlines()

    for line in lines:
        if line not in seen:
            seen.add(line)

            features = extract_features(line)
            prediction = model.predict([features])

            if prediction[0] == -1:
                print("🚨 Anomaly detected:", line.strip())
                with open("anomalies.log", "a") as out:
                    out.write(line)

    time.sleep(2)
