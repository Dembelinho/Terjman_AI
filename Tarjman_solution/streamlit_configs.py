import streamlit as st
def initialize_session_storage():
    if "history" not in st.session_state:
        st.session_state.history = []

def read_from_session_state():
    for hist in st.session_state.history:
        with st.chat_message(hist["role"]):
            st.write(hist["query"])
def save_msg(role: str, message: str):
    st.session_state.history.append({"role": role, "query": message})
