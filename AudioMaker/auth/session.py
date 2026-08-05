import streamlit as st


def get_current_user():

    if "discord_user" in st.session_state:

        return st.session_state["discord_user"]

    return None