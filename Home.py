import streamlit as st

st.set_page_config(page_title="Shaiju's Portfolio", page_icon="📁")
page = st.sidebar.selectbox("Navigate", ["Home", "Projects", "Blogs", "Contact"])


st.title("👩‍💻 Shaiju Shajahan")
st.subheader("Software Sales Consultant | Learning AI, Automation & Data Apps")

st.markdown("""
Welcome to my personal tech journey space!  
This portfolio highlights projects I've built while learning Python, AI, and automation.

👉 Use the sidebar to explore my [Projects](./Projects), [Blogs](./Blog), or [Contact](./Contact).
""")
