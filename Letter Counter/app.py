import streamlit as st

st.title("Letter Counter")

text = st.text_area("Paste your text here")

amount = len(text)

st.write(amount)