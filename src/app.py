import streamlit as st
from chat import chatbot
from pdfReader import pdfReader

# app config
st.set_page_config(page_title="You need me", page_icon="😏")

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Choose an option", ["Home", "Chat with me :)", "Help with docs?"])

if selection == "Home":
    st.title("Hey wassup?")
    st.write("Use the sidebar to navigate between")
elif selection == "Chat with me :)":
    with st.spinner("Loading Chatbot..."):
        # st.title("Chat with me :)")
        chatbot()
elif selection == "Help with docs?":
    with st.spinner("Loading PDF Reader..."):
        # st.title("Help with docs?")
        pdfReader()
