import streamlit as st
import os
import requests
import streamlit as st

import gspread
st.set_page_config(layout="wide")


st.markdown(
    """
    <style>
    .stApp {
        background-color: #0000;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)


def home():
    left_column, right_column = st.columns(2)
    with left_column:
              st.title("Hi, I'm Sangbed")
              st.write(" ")
    
              st.write("I’m a videographer and photographer who loves turning everyday moments into engaging visual stories.") 
              st.write("I create content around running, workouts, and vlogs, while also pursuing my final year in Computer Science Engineering.")
              st.write("I enjoy combining creativity, storytelling, and technology to create videos that feel authentic and impactful.")
              
          # 3. Add elements to the right column
    with right_column:
              st.image("personal.jpg", caption="Welcome")


def instagram():
        st.iframe("""
<style>
html, body {
    margin: 0;
    overflow: hidden;
}

.carousel {
    width: 100%;
    overflow: hidden;
}

.track {
    display: flex;
    gap: 20px;
    width: max-content;
    animation: slide 130s linear infinite;
}

.card {
    width: 180px;
    height: 400px;
    flex-shrink: 0;
    overflow: hidden;
    border-radius: 12px;
}

iframe {
    width: 100%;
    height: 100%;
    border: 0;
}

@keyframes slide {
    0% {
        transform: translateX(0);
    }

    100% {
        transform: translateX(-100%);
    }
}
</style>

<div class="carousel">
    <div class="track">

        <div class="card"><iframe src="https://www.instagram.com/p/DctXaAkSloW/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/p/DcsLFmtziRb/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/p/DcqnokvTICk/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/p/Dcdp9dDJOiA/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DcsLFmtziRb/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DcZ54-Yhokd/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/Db5l4cjE_lx/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/Dbs0iFfIznG/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbZ2wwYxYJK/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbGGJWipfhv/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbDwS4DvZhF/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbAAi4XBjKx/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/Dar73G-JoUO/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DaSDk6MMP5u/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DaC35hxzqox/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZ5ajULT15g/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZuoGVyTODx/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZthf9szO1r/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZotNbxTuzf/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZjf0m0zW9S/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZaQfB3zXEF/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/Db5l4cjE_lx/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/Dbs0iFfIznG/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbZ2wwYxYJK/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbGGJWipfhv/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbDwS4DvZhF/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbAAi4XBjKx/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/Dar73G-JoUO/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DaSDk6MMP5u/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DaC35hxzqox/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZ5ajULT15g/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZuoGVyTODx/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZthf9szO1r/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZotNbxTuzf/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZjf0m0zW9S/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZaQfB3zXEF/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/p/DctXaAkSloW/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/p/DcsLFmtziRb/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/p/DcqnokvTICk/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/p/Dcdp9dDJOiA/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DcsLFmtziRb/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DcZ54-Yhokd/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/Db5l4cjE_lx/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/Dbs0iFfIznG/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbZ2wwYxYJK/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbGGJWipfhv/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbDwS4DvZhF/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbAAi4XBjKx/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/Dar73G-JoUO/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DaSDk6MMP5u/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DaC35hxzqox/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZ5ajULT15g/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZuoGVyTODx/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZthf9szO1r/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZotNbxTuzf/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZjf0m0zW9S/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZaQfB3zXEF/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/Db5l4cjE_lx/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/Dbs0iFfIznG/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbZ2wwYxYJK/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbGGJWipfhv/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbDwS4DvZhF/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DbAAi4XBjKx/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/Dar73G-JoUO/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DaSDk6MMP5u/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DaC35hxzqox/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZ5ajULT15g/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZuoGVyTODx/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZthf9szO1r/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZotNbxTuzf/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZjf0m0zW9S/embed"></iframe></div>
        <div class="card"><iframe src="https://www.instagram.com/reel/DZaQfB3zXEF/embed"></iframe></div>

    </div>
</div>
""", height=320)

def spacce():
       st.write("")
       st.write("")
def contact():
    credentials = st.secrets["gcp_service_account"]
    gc = gspread.service_account_from_dict(credentials)
    sheet = gc.open("Portfolio Contact Messages").sheet1
    left, right = st.columns(2)
    with left:
           st.title("Contact me")
           st.write("Feel Free to reach out:-")
    with right:
           with st.form("Contact form"):
                name = st.text_input("Your Name")
                email = st.text_input("Your Email Address")
                number = st.text_input("Your contact number")
                message = st.text_area("Your Message")
                
                submit_button = st.form_submit_button("Send Message")
                if submit_button:
                      if not name or not email or not message:
                              st.warning("Please fill out all fields bfore submiting")
                      else:
                             sheet.append_row([name, email, message, number])
                             st.success(f"Thank you {name}! Your message has been sent")
                       

home()
spacce()
instagram()
spacce()
contact()