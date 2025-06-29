import streamlit as st

st.title("💻 Projects")
def show_projects():
    st.title("Projects")
    st.subheader("💰 Expense Tracker App")

    st.markdown("""
    This is a simple Expense Tracker app built with **Streamlit** and **Python**.

    **Features:**
    - Add and categorize expenses
    - View monthly summaries
    - Visual charts using `matplotlib` or `altair`
    - Data stored locally in CSV (or you can link it to Google Sheets)

    🔗 [View Code on GitHub](https://github.com/Shaiju786/expense-tracker)  
    ▶️ [Try it Live](https://expense-tracker.streamlit.app/)
    """)

    st.image("https://github.com/Shaiju786/expense-tracker/raw/main/demo.png", caption="Expense Tracker Demo", use_column_width=True)
st.header("1. Simple Expense Tracker (Streamlit)")
st.markdown("""
A beginner-friendly web app to add, view, and analyze personal expenses.

**Tech Stack:** Python, Streamlit, Pandas  
**Features:** Add expense, View summary, Visualize spending by category  
**Live App:** *[Insert link]*  
**Code:** [GitHub Repo](https://github.com/Shaiju786/expense-tracker-streamlit)

**What I Learned:**
- Built a working app from scratch
- Replaced CLI inputs with web UI (st.text_input, st.number_input)
- Deployed using Streamlit Cloud
""")
