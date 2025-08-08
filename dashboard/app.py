import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from ingest.cloudtrail_ingest import load_logs_from_folder
from detection.model import ThreatDetector


st.set_page_config(layout="wide", page_title="Cloud Threat Detector Dashboard")

st.title("☁️🔍 Cloud Threat Detector Dashboard")
st.markdown("View ingested AWS CloudTrail logs and detected anomalies.")

# Load and process data
df = load_logs_from_folder("data/sample_logs")

detector = ThreatDetector()
detector.fit(df)
result_df = detector.predict(df)

# Sidebar Filters
st.sidebar.header("🔍 Filters")
user_filter = st.sidebar.multiselect("User", result_df["user"].unique())
action_filter = st.sidebar.multiselect("Action", result_df["action"].unique())
ip_filter = st.sidebar.text_input("IP contains", "")

filtered_df = result_df.copy()

if user_filter:
    filtered_df = filtered_df[filtered_df["user"].isin(user_filter)]
if action_filter:
    filtered_df = filtered_df[filtered_df["action"].isin(action_filter)]
if ip_filter:
    filtered_df = filtered_df[filtered_df["ip"].str.contains(ip_filter)]

# Display
st.subheader("📄 All Events")
st.dataframe(filtered_df, use_container_width=True)

st.subheader("🚨 Anomalies Only")
anomalies = filtered_df[filtered_df["is_anomaly"] == 1]

if not anomalies.empty:
    st.warning(f"{len(anomalies)} anomalies detected.")
    st.dataframe(anomalies, use_container_width=True)
else:
    st.success("No anomalies found in filtered results.")

# Charts Section
st.subheader("📊 Chart: Most Frequent Actions")
action_counts = df["action"].value_counts().head(10)
st.bar_chart(action_counts)

st.subheader("📊 Chart: Actions by User")
user_action_counts = df.groupby("user")["action"].count()
st.bar_chart(user_action_counts)

