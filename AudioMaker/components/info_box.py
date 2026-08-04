import streamlit as st


def show_info_box(title, message):

    with st.expander(f"ℹ️ {title}"):

        st.markdown(
            message
        )