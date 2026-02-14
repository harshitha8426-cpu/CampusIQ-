
import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(layout="wide")
st.title("🏙 CampusIQ Command Center")

API_URL = "http://127.0.0.1:8000/api/dashboard"
data_log = []

while True:
    try:
        response = requests.get(API_URL)
        data = response.json()
        data_log.append(data)
        df = pd.DataFrame(data_log)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Crowd Density", data["crowd"])
        col2.metric("Waste Level", data["waste"])
        col3.metric("Equipment Runtime", data["runtime"])
        col4.metric("Risk Level", data["risk_level"])

        st.line_chart(df[["crowd", "waste"]])
        time.sleep(5)
    except:
        st.error("Backend not running.")
        break
