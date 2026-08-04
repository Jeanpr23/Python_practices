import uuid
import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

cookies = EncryptedCookieManager(
    prefix="AudioMaker/",
    password=""
)

def get_visitor_id():

    if not cookies.ready():
        st.info("Loading visitor cookie...")
        st.stop()

    if "visitor_id" in cookies:

       visitor_id = cookies["visitor_id"]


    else:

        visitor_id = str(uuid.uuid4())

        cookies["visitor_id"] = visitor_id

        cookies.save()

    return visitor_id
