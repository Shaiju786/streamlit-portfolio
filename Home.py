import streamlit as st
from projects import show_projects  # 👈 Add this line

st.set_page_config(page_title="Shaiju's Portfolio", layout="wide")

st.sidebar.title("Navigate")
selection = st.sidebar.radio("Go to", ["Home", "Projects", "Blogs", "Contact"])

if selection == "Home":
    st.title("Hi, I'm Shaiju!")
    st.write("Welcome to my portfolio. Use the sidebar to explore.")
elif selection == "Projects":
    show_projects()  # 👈 Update this
elif selection == "Blogs":
    st.subheader("Blogs")
    st.write("Blog content goes here...")
elif selection == "Contact":
    st.subheader("Contact")
    st.write("You can reach me at shaiju@example.com")

