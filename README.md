
# Sentinel Log Anomaly Detection Dashboard

🚨 **Sentinel** is a modular, real-time log anomaly detection system built using **Python and Streamlit**.  
It includes log preprocessing, feature extraction, model training, anomaly detection, and an interactive dashboard.

---

## 📁 Project Structure

```

sentinel_project/
│
├── train.py              # Train anomaly detection model
├── sentinel.py           # Core anomaly detection engine
├── features.py           # Log feature extraction logic
├── dashboard.py          # Streamlit dashboard
├── config.yaml           # Configuration settings
├── sample.log            # Sample input logs
├── anomalies.log         # Detected anomalies (auto-created)
├── model.pkl             # Trained ML model (auto-created)
├── vectorizer.pkl        # Feature vectorizer (auto-created)
└── requirements.txt      # Project dependencies

````

---

## 🚀 Features

- Modular architecture (training, detection, dashboard separated)
- Log feature extraction pipeline
- Machine-learning–based anomaly detection
- Auto-generated anomaly log file
- Interactive Streamlit dashboard
- Configurable settings via `config.yaml`
- Clean, readable UI suitable for SOC / SIEM demos

---

## 🛠️ Tech Stack

- **Python**
- **Scikit-learn**
- **Pandas**
- **Streamlit**
- **YAML**

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/sentinel-project.git
cd sentinel_project
````

### 2️⃣ Create a virtual environment (recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run (Commands)

### 🔹 Step 1: Train the model

This step generates `model.pkl` and `vectorizer.pkl`.

```bash
python train.py
```

---

### 🔹 Step 2: Run anomaly detection

Processes logs and writes anomalies to `anomalies.log`.

```bash
python sentinel.py
```

---

### 🔹 Step 3: Launch the dashboard

Starts the Streamlit web interface.

```bash
streamlit run dashboard.py
```

Open your browser at:

```
http://localhost:8501
```

---

## ⚙️ Configuration

All runtime parameters (paths, thresholds, refresh rates, etc.) are defined in:

```bash
config.yaml
```

You can modify this file to:

* Change anomaly thresholds
* Update file paths
* Tune model behavior

---

## 📊 How It Works

1. **Feature Extraction**

   * `features.py` parses logs and converts them into numerical features

2. **Model Training**

   * `train.py` trains an anomaly detection model
   * Saves trained model and vectorizer

3. **Anomaly Detection**

   * `sentinel.py` loads the model
   * Detects anomalies and logs them

4. **Visualization**

   * `dashboard.py` displays real-time metrics and alerts

---

## 🎓 Use Cases

* Academic SIEM / SOC projects
* Cybersecurity research
* Log monitoring simulations
* ML anomaly detection demos
* Streamlit dashboard portfolios

---

## 🔮 Future Enhancements

* Live log ingestion
* Deep learning anomaly models
* Severity-based classification
* Alert notifications (Email / Slack)
* Cloud deployment
* Role-based access control

---
## 📸 Screenshots

### 🔹 Main Dashboard View
![Sentinal Dashboard](screenshots/dashboard.png)

## 🎥 Demo Video (Screen Recording)

▶️ Live dashboard demonstration showing:
- Real-time stock price updates  
- Volume & volatility graphs  
- Alert trigger with sound and red highlight  
- Stock switching (AAPL, TSLA, AMZN, GOOGL, MSFT)

🔗 Watch the demo:  
https://drive.google.com/file/d/1s3AZEOQr6wn2ky4yae1oU69sTFU9eeuA/view?usp=sharing

## 🏢 Developed During Internship

This project was developed as part of an internship at **Infotact Solutions**, under the guidance and mentorship provided during the internship period.

**Organization:** Infotact Solutions  
**Project Type:** Internship Project  
**Role:** Python Development Intern



