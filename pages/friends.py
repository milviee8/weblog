from PIL import Image
import requests

import streamlit as st

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.title("My Companions ཐིཋྀ")


import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/friend 1.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

     # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/friend 4.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)
with text_column:
    st.write(""" My life is a tapestry, with longstanding friendships that stretch back to my first year of seventh grade. I have a special place in my heart for these pals since they have stood by me during the challenging times of youth. 
             Their presence has always brought joy, encouragement, and enduring memories that have stood the test of time. 
             In addition to these treasured pals, unexpected friends have come together with me to form a seamless whole, bringing vivid colors to the picture of my existence. 
             It's amazing how relationships may develop out of the blue, forging ties that endure the uncertainty of life's path. However, I also have friends that I haven't included in the picture.
             """)
  # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/friend 3.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)
 # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/igorot.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 1))
with image_column:
    st.image(img_contact_form)
