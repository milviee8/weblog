import streamlit as st

st.set_page_config(
    page_title="Multipage app",
    page_icon="wave",
)

st.title("Main page")
st.sidebar.success("Select a page above")

from PIL import Image
import requests

import streamlit as st

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.title("MILVI's Blog")


import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/homepage.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with st.container():
    st.subheader("HI, I AM MILVI M. ADAJAR •ᴗ•")
    st.write(" 18 years old, living at CAGDIANAO, DINAGAT ISLANDS. I was born on FEBRUARY 18, 2005, and I am currently studying at Surigao del Norte State University under the program of Computer Engineering.")
    st.write( "I am  a simple person with an ambition.")
    st.subheader("This is my socials feel free to visit them.")
    st.write(" ▶ Facebook: https://www.facebook.com/milvi.adajar")
    st.write(" ▶ Instagram: whosxmilvi")
    st.write(" ▶Email: adajarmilvi3@gmail.com")
    st.write(" ▶Contact Number: 09123204628")








