import streamlit as st
from config import ENABLE_MANIPULATION

if not ENABLE_MANIPULATION:
    st.warning("This pae is currently disabled.")
    st.stop()

    
from russian_twisters import generate_russian_twister
from japanese_twisters import generate_japanese_twister
from tts.speech_generator import generate_audio
from audio.merge_audio import merge_audio
from cleanup import clean_folder
from auth.session import get_current_user
from components.info_box import show_info_box
from config import FREE_MODE

if not FREE_MODE:
    
    create_database()

clean_folder("uploads", 24)
clean_folder("generated", 24)


st.set_page_config(
    page_title="Manipulation",
    page_icon="🗣️",
    layout="centered"
)

if not FREE_MODE:
    discord_user = get_current_user()

    visitor_id = get_visitor_id()

    st.write("Visitor ID:", visitor_id)

    account = get_current_account(
        discord_user,
        visitor_id
    )

    login_url = get_discord_login_url()

    if discord_user:

       username = discord_user["global_name"]

       st.link_button(
          f"🟢 Login as {username}",
          login_url

        )

    else:

     st.link_button(
        "🔵 Login with Discord",
        login_url
    )

    query_params = st.query_params

    code = query_params.get("code")


    if code:

        token_data = get_access_token(code)

        if "access_token" in token_data:

            access_token = token_data["access_token"]

            user = get_discord_user(access_token)

            st.session_state["discord_user"] = user

            create_user(
               discord_id=user["id"],
               username=user["global_name"]
            )

            st.rerun()


st.markdown(
    "<h1 style='text-align: center;'>Manipulation</h1>",
    unsafe_allow_html=True
)

show_info_box(
    "What is Manipulation?",
    """
    “Audio manipulation can alter a recording in ways that make it more difficult for Roblox’s
     moderation systems to detect offensive language present in a song when the audio is
     uploaded.”
    """
)

audio_file = st.file_uploader(
    "📂 Upload audio file",
    type=["mp3", "wav", "ogg"]
)

if audio_file:

    user_audio_path = "uploads/user_audio.mp3"

    with open(user_audio_path, "wb") as f:
        f.write(audio_file.getbuffer())

language = st.selectbox(
    "Choose manipulation language",
    [
        "Russian",
        "Japanese"
    ]
)

if not FREE_MODE:

    uses = get_usage(
    account["id"],
    "manipulation"
)
    st.write(
        f"{uses}/5 uses"
    )

generate_button = st.button("Generate manipulation")

if generate_button:

    if not FREE_MODE:

     if not can_use(
        account["id"],
        "manipulation"
    ):
        st.error(
            "You have reached today's limit."
        )

    elif not audio_file:

        st.warning(
            "Please upload an audio file first"
        )


    else:

        # Generate tongue twister

        if language == "Russian":

            twister = generate_russian_twister()

        else:

            twister = generate_japanese_twister()



        # Create tts

        tts_path = "generated/tongue_twister.mp3"


        generate_audio(
           twister,
           language,
           tts_path
        )

        final_path = "generated/finished.mp3"

        merge_audio(
            tts_path,
            user_audio_path,
            final_path
        )

        if not FREE_MODE:

            add_usage(
                account["id"],
                "manipulation"
            ) 

            

        st.success("Manipulation applied successfully!")

        st.audio(final_path)


if audio_file:
    st.success("File received successfully")

    st.audio(audio_file)
