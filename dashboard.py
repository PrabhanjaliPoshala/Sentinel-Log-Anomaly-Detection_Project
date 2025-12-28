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

# ---------------- AUTO REFRESH ----------------
st_autorefresh(interval=5000, key="refresh")

# ---------------- CSS (WHITE THEME) ----------------
st.markdown("""
<style>
.stApp { background-color: #ffffff; color: #0d1117; }
section[data-testid="stSidebar"] { background-color: #f6f8fa; }
section[data-testid="stSidebar"] * { color: #0d1117 !important; }
h1, h2 { color: #0969da !important; }

div[data-testid="stMetric"] {
    background-color: white;
    padding: 16px;
    border-radius: 10px;
    border: 1px solid #d0d7de;
}

.stAlert {
    background-color: #fff5f5 !important;
    color: #cf222e !important;
    border: 1px solid #cf222e;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TTS FUNCTION ----------------
def tts_speak(text):
    js = f"""
    <script>
    var msg = new SpeechSynthesisUtterance("{text}");
    msg.lang = 'en-US';
    window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js, height=0)

# ---------------- TITLE ----------------
st.title("🚨 Sentinel Log Anomaly Detection Dashboard")
st.caption("Real-time Security Monitoring System")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙ Control Panel")
anomaly_threshold = st.sidebar.slider("Anomaly Probability (%)", 10, 90, 40)
enable_voice = st.sidebar.checkbox("🗣️ Enable Voice Alerts", value=False)

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

if "last_alert_ts" not in st.session_state:
    st.session_state.last_alert_ts = None

st.session_state.logs.append(generate_log())
df = pd.DataFrame(st.session_state.logs[-20:])

# ---------------- METRICS ----------------
total_logs = len(st.session_state.logs)
anomalies = sum(1 for log in st.session_state.logs if log["Anomaly"] == "YES")
normal = total_logs - anomalies

c1, c2, c3 = st.columns(3)
c1.metric("📄 Total Logs", total_logs)
c2.metric("🚨 Anomalies", anomalies)
c3.metric("✅ Normal Events", normal)

# ---------------- ALERT + VOICE ----------------
if df.iloc[-1]["Anomaly"] == "YES":
    ts = df.iloc[-1]["Timestamp"]
    st.error("🚨 CRITICAL ALERT: Suspicious activity detected!")

    if enable_voice and st.session_state.last_alert_ts != ts:
        tts_speak("Warning. Anomaly detected in system logs.")
        st.session_state.last_alert_ts = ts

# ---------------- TABLE ----------------
st.subheader("📊 Recent Log Activity")
st.dataframe(df, use_container_width=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("© 2025 Sentinel Security System | Academic SIEM Project")
