import streamlit as st

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
