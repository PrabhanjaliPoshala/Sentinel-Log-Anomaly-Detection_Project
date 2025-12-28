import pickle

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def extract_features(log_line):
    return vectorizer.transform([log_line]).toarray()[0]
