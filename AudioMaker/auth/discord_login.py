import requests
import streamlit as st

DISCORD_CLIENT_ID = st.secrets["DISCORD_CLIENT_ID"]
DISCORD_CLIENT_SECRET = st.secrets["DISCORD_CLIENT_SECRET"]
DISCORD_REDIRECT_URI = st.secrets["DISCORD_REDIRECT_URI"]


def get_discord_login_url():

    discord_url = (
        "https://discord.com/oauth2/authorize?"
        f"client_id={DISCORD_CLIENT_ID}"
        "&response_type=code"
        f"&redirect_uri={DISCORD_REDIRECT_URI}"
        "&scope=identify"
    )

    return discord_url


def get_access_token(code):

    data = {

        "client_id": DISCORD_CLIENT_ID,

        "client_secret": DISCORD_CLIENT_SECRET,

        "grant_type": "authorization_code",

        "code": code,

        "redirect_uri": DISCORD_REDIRECT_URI
    }

    headers = {

        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(

        "https://discord.com/api/oauth2/token",

        data=data,

        headers=headers
    )


    return response.json()



def get_discord_user(access_token):

    headers = {

        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(

        "https://discord.com/api/users/@me",

        headers=headers
    )

    return response.json()