import streamlit as st
import pandas as pd
import random
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sentinel | Log Anomaly Dashboard",
    layout="wide",
    page_icon="🚨"
)

# ---------------- WHITE MODE CSS ----------------
st.markdown("""
<style>

/* Main app background */
.stApp {
    background-color: #ffffff;
    color: #0d1117;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #f6f8fa;
    color: #0d1117;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: #0d1117 !important;
}

/* Headers */
h1, h2, h3, h4, h5, h6 {
    color: #0969da !important;
    font-weight: 600;
}

/* Normal text */
p, span, label, div {
    color: #0d1117;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background-color: #ffffff;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #d0d7de;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}

/* Metric labels */
div[data-testid="stMetricLabel"] {
    color: #57606a !important;
}

/* Buttons */
.stButton > button {
    background-color: #0969da;
    color: #ffffff !important;
    border-radius: 8px;
    border: none;
    font-weight: 600;
}

/* Slider */
div[data-baseweb="slider"] * {
    color: #0d1117 !important;
}

/* Alerts */
.stAlert {
    background-color: #fff5f5 !important;
    color: #cf222e !important;
    border: 1px solid #cf222e;
}

/* Tables */
thead tr th {
    background-color: #f6f8fa !important;
    color: #0969da !important;
    font-weight: 600;
}

tbody tr td {
    background-color: #ffffff !important;
    color: #0d1117 !important;
}

/* Streamlit top bar */
header, header * {
    background-color: #ffffff !important;
    color: #0d1117 !important;
}

/* Footer */
footer {
    visibility: hidden;
}

/* ========================= */
/* THREE-DOTS MENU */
/* ========================= */
div[data-baseweb="popover"] {
    background-color: #ffffff !important;
}

div[role="menu"] {
    background-color: #ffffff !important;
    color: #000000 !important;
}

div[role="menu"] * {
    color: #000000 !important;
    font-weight: 500;
}

div[role="menu"] div:hover {
    background-color: #f6f8fa !important;
}

/* ========================= */
/* DATAFRAME DOWNLOAD */
/* ========================= */
button[data-testid="stDownloadButton"] {
    background-color: #f6f8fa !important;
    color: #0d1117 !important;
    border: 1px solid #d0d7de;
}

button[data-testid="stDownloadButton"] svg {
    fill: #0d1117 !important;
}

button[data-testid="stDownloadButton"]:hover {
    background-color: #eaeef2 !important;
}

/* Dataframe container */
div[data-testid="stDataFrame"] {
    border-radius: 12px;
    border: 1px solid #d0d7de;
    background-color: #ffffff;
}

</style>
""", unsafe_allow_html=True)

# ---------------- AUTO REFRESH ----------------
st_autorefresh(interval=5000, key="refresh")

# ---------------- TITLE ----------------
st.title("🚨 Sentinel Log Anomaly Detection Dashboard")
st.caption("Real-time Security Monitoring System")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙ Control Panel")
anomaly_threshold = st.sidebar.slider(
    "Anomaly Probability (%)",
    min_value=10,
    max_value=90,
    value=40
)

# ---------------- LOG GENERATOR ----------------
def generate_log():
    return {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Source IP": f"192.168.1.{random.randint(1,255)}",
        "Event Type": random.choice(
            ["LOGIN", "LOGOUT", "FILE_ACCESS", "ERROR", "PASSWORD_FAIL"]
        ),
        "Anomaly": "YES" if random.randint(1,100) < anomaly_threshold else "NO"
    }

# ---------------- SESSION STATE ----------------
if "logs" not in st.session_state:
    st.session_state.logs = []

st.session_state.logs.append(generate_log())
df = pd.DataFrame(st.session_state.logs[-20:])

# ---------------- METRICS ----------------
total_logs = len(st.session_state.logs)
anomalies = sum(1 for log in st.session_state.logs if log["Anomaly"] == "YES")
normal = total_logs - anomalies

c1, c2, c3 = st.columns(3)
c1.metric("📄 Total Logs", total_logs)
c2.metric("🚨 Anomalies Detected", anomalies)
c3.metric("✅ Normal Events", normal)

# ---------------- ALERT ----------------
if df.iloc[-1]["Anomaly"] == "YES":
    st.error("🚨 CRITICAL ALERT: Suspicious activity detected!")

# ---------------- TABLE ----------------
st.subheader("📊 Recent Log Activity")
st.dataframe(df, use_container_width=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("© 2025 Sentinel Security System | Academic SIEM Project")
