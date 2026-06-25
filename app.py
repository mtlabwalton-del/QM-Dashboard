import streamlit as st
import pandas as pd
from urllib.parse import quote

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="QM Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# GOOGLE SHEET ID
# -----------------------------
SHEET_ID = "1yUgLvwouZBV00v2Y7uf6GCI0eTFmyawZOrQ6OODzb-0"

# -----------------------------
# LOAD GOOGLE SHEET
# -----------------------------
@st.cache_data(ttl=60)
def load_sheet(sheet_name):

    sheet = quote(sheet_name)

    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={sheet}"

    return pd.read_csv(url)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("📊 QM Dashboard")

page = st.sidebar.radio(
    "Select Dashboard",
    [
        "Monthly Gauge Monitoring Plan",
        "Gauge Health Inspection Index",
        "Gauge Servicing Index",
        "Gauge Development Index"
    ]
)

# -----------------------------
# PAGE 1
# -----------------------------
if page == "Monthly Gauge Monitoring Plan":

    st.title("Monthly Gauge Monitoring Plan")

    df = load_sheet("Monthly Gauge Monitoring Plan")

    st.dataframe(df, use_container_width=True)

# -----------------------------
# PAGE 2
# -----------------------------
elif page == "Gauge Health Inspection Index":

    st.title("Gauge Health Inspection Index")

    df = load_sheet("Gauges health inspection Index")

    st.dataframe(df, use_container_width=True)

# -----------------------------
# PAGE 3
# -----------------------------
elif page == "Gauge Servicing Index":

    st.title("Gauge Servicing Index")

    df = load_sheet("Gauge Servicing Index")

    st.dataframe(df, use_container_width=True)

# -----------------------------
# PAGE 4
# -----------------------------
elif page == "Gauge Development Index":

    st.title("Gauge Development Index")

    df = load_sheet("Gauge Development Index")

    st.dataframe(df, use_container_width=True)
