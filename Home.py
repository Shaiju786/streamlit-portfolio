import streamlit as st

# Page setup
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
    st.title("🛠️ My Projects")

    st.subheader("💸 Expense Tracker App")
    st.write("""
    A simple Streamlit app to manage and visualize personal expenses.  
    **Tech Stack:** Python, Streamlit, Pandas  
    🔗 [GitHub Repo](https://github.com/Shaiju786/expense-tracker)
    """)

    st.subheader("🔍 Google Search Console to Google Sheets Automation")
    st.write("""
    Automates pulling Google Search Console data into Google Sheets using Python and Google APIs.  
    **Tech Stack:** Python, GSC API, gspread  
    🚧 Coming Soon
    """)

    st.subheader("📦 Logi-Sys Sales Workflow Explainer")
    st.write("""
    Internal project for demoing the freight ERP workflow, showcasing digital transformation potential.  
    **Format:** Interactive walkthrough (Not public)
    """)

# ------------------------
# Section: Blogs
# ------------------------
elif selection == "Blogs":
    st.title("📚 Blogs")

    st.write("🚧 Coming soon! I’ll be sharing tutorials and reflections on learning Python, automation, and tech.")

# ------------------------
# Section: Contact
# ------------------------
elif selection == "Contact":
    st.title("📬 Contact Me")

    st.markdown("""
    - 📧 Email: shaiju@example.com  
    - 💼 [LinkedIn](https://www.linkedin.com/in/shaiju-shajahan)  
    - 🐙 [GitHub](https://github.com/Shaiju786)

    Feel free to reach out for collaboration or just to connect!
    """)

