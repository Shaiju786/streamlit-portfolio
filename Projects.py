import streamlit as st

st.set_page_config(page_title="Projects | Shaiju's Portfolio", layout="wide")

st.title("🛠️ My Projects")

st.markdown("""
Welcome to my projects page! Here are a few of the apps and automations I've worked on as I learn and apply Python, Streamlit, and automation tools.
""")

# -------------------
# Project 1: Expense Tracker
# -------------------
st.subheader("💸 Expense Tracker App")
st.write("""
This is a personal finance tool to track monthly expenses, categorize them, and visualize spending.

**Tech Stack:**  
- Python  
- Streamlit  
- Pandas  

[🔗 GitHub Repo](https://github.com/Shaiju786/expense-tracker)
""")

# -------------------
# Project 2: GSC to Sheets
# -------------------
st.subheader("🔍 Google Search Console to Google Sheets")
st.write("""
An automation that pulls data from Google Search Console and writes it into Google Sheets using Python and APIs.

**Tech Stack:**  
- Python  
- Google Search Console API  
- gspread / pygsheets  

Coming soon — will be shared on GitHub.
""")

# -------------------
# Add More Projects
# -------------------
st.info("More projects will be added as I build and explore!")

