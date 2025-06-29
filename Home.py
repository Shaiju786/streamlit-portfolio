import streamlit as st

st.set_page_config(page_title="Shaiju's Portfolio", layout="wide")

# Sidebar menu
st.sidebar.title("Navigate")
selection = st.sidebar.radio("Go to", ["Home", "Projects", "Blogs", "Contact"])

# Display corresponding page
if selection == "Home":
    st.title("Hi, I'm Shaiju!")
    st.write("Welcome to my portfolio. Use the sidebar to explore.")
elif selection == "Projects":
    st.subheader("Projects")
    st.write("List of projects will appear here...")
elif selection == "Blogs":
    st.subheader("Blogs")
    st.write("Blog content goes here...")
elif selection == "Contact":
    st.subheader("Contact")
    st.write("You can reach me at shaiju@example.com")
    
