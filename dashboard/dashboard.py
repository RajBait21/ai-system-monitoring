import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import time

st.set_page_config(
    page_title="AI System Monitoring Dashboard",
    layout="wide"
)

st.title("AI Real-Time System Monitoring Dashboard")

API_URL = "https://ai-system-monitoring.onrender.com/metrics"

refresh = st.button("Refresh Dashboard")

try:
    response = requests.get(API_URL)
    data = response.json()

    if data:
        df = pd.DataFrame(data)
        df["created_at"] = pd.to_datetime(df["created_at"])

        latest = df.iloc[0]

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("CPU Usage", f"{latest['cpu_usage']:.2f}%")
        col2.metric("Memory Usage", f"{latest['memory_usage']:.2f}%")
        col3.metric("Disk Usage", f"{latest['disk_usage']:.2f}%")
        col4.metric("Predicted Risk", latest["predicted_risk"])

        st.subheader("CPU Usage Over Time")
        fig_cpu = px.line(
            df.sort_values("created_at"),
            x="created_at",
            y="cpu_usage",
            markers=True
        )
        st.plotly_chart(fig_cpu, use_container_width=True)

        st.subheader("Memory Usage Over Time")
        fig_memory = px.line(
            df.sort_values("created_at"),
            x="created_at",
            y="memory_usage",
            markers=True
        )
        st.plotly_chart(fig_memory, use_container_width=True)

        st.subheader("Risk Level Distribution")
        fig_risk = px.histogram(
            df,
            x="predicted_risk"
        )
        st.plotly_chart(fig_risk, use_container_width=True)

        st.subheader("Latest Monitoring Records")
        st.dataframe(df)

    else:
        st.warning("No monitoring data available. Start the collector first.")

except Exception as error:
    st.error(f"Backend is not running: {error}")

time.sleep(2)
st.rerun()