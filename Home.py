import streamlit as st

# Set page configuration
st.set_page_config(page_title="Shaiju's Portfolio", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigate")
selection = st.sidebar.radio("Go to", ["Home", "Projects", "Blogs", "Contact"])

# ------------------------
# Section: Home
# ------------------------
if selection == "Home":
    st.title("Hi, I'm Shaiju!")
    st.write("""
        Welcome to my portfolio.  
        I'm a tech learner and AI enthusiast with a background in logistics software consulting.  
        This site showcases my journey into automation, Python, and data projects.

        👉 Use the **sidebar** to explore my **Projects**, **Blogs**, or **Contact** information.
    """)

# ------------------------
# Section: Projects
# ------------------------
elif selection == "Projects":
    st.title("Projects")

    st.subheader("1. Expense Tracker App")
    st.write("""
    A simple app to track your expenses and categorize spending.  
    **Tools:** Streamlit, Python, Pandas  
    [View Code on GitHub](https://github.com/Shaiju786/expense-tracker)
    """)

    st.subheader("2. Google Search Console → Sheets Automation")
    st.write("""
    Pulls data from Google Search Console into Google Sheets using Python and the GSC API.  
    **Tools:** Python, Google API, gspread  
    [Coming Soon]
    """)

# ------------------------
# Section: Blogs
# ------------------------
elif selection == "Blogs":
    st.title("Blogs")

    st.write("🚧 Coming soon! I’ll be sharing learnings from my coding and automation journey here.")

# ------------------------
# Section: Contact
# ------------------------
elif selection == "Contact":
    st.title("Contact Me")

    st.write("""
    📧 Email: shaiju@example.com  
    💼 [LinkedIn](https://www.linkedin.com/in/shaiju-shajahan)  
    🐙 [GitHub](https://github.com/Shaiju786)
    """)

    st.write("Feel free to connect or drop me a message!")

