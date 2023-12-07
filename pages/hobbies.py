from PIL import Image
import requests

import streamlit as st

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.title("HOBBIES ꩜")
st.subheader("Dancing")


import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/dance 1.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 1))
with image_column:
    st.image(img_contact_form)


    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/dance 2.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 1))
with image_column:
    st.image(img_contact_form)

  # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/dance 3.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 1))
with image_column:
    st.image(img_contact_form)
with st.container():
  st.write("Dance has been an intrinsic part of my essence since the days when I was just a little, discovering the magic of movement. The rhythm of music became the heartbeat of my passion, and as I embraced the dance floor, an exhilarating connection unfolded. Over the years, my love for dance has blossomed into a journey of self-expression and creativity. The joy of choreography and the freedom of movement have been my constant companions, guiding me through the highs and lows of life. Winning in dance contests has not only been a testament to dedication and hard work but also a celebration of the sheer bliss that comes with translating emotions into dance. Each step, each twirl, carries a piece of my story, and the dance floor becomes a canvas where my heart paints its most authentic colors.")

st.subheader("Music & Movies")


import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/hobbies 1.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 1))
with image_column:
    st.image(img_contact_form)


    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/hobbies 2.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 1))
with image_column:
    st.image(img_contact_form)

with st.container():
  st.write("I find that immersing myself in the entrancing realm of music offers a meaningful release and a channel for emotional connection. I have a particular spot in my heart for James Arthur among all the artists. His heartfelt lyrics and beautiful voice speak to me on a very deep personal level, providing a soundtrack to the moments in my life. With every note seeming like an emotional journey, his music has become a constant companion that wovens itself into a part of my life. In addition, I adore several genres in movies. I get great pleasure in experimenting with different genres, letting cinematic storytelling mold and color the experience, whether it's the gripping story of a drama or the thrilling moments of an action-packed movie.")

st.subheader("SPORT (Lawn Tennis)")


import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/sport.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 1))
with image_column:
    st.image(img_contact_form)


with st.container():
  st.write("Entering the world of lawn tennis for a short while and finding it interesting has been an interesting chapter in my life. My interest in the game caught by the clear sound of the ball hitting the strings and the lively back-and-forth play on the court. Playing tennis for a short while turned into a fun experiment with technique and tactics. Even though I haven't played lawn tennis for very long, the experience has been unforgettable since it introduced me to a sport that is the perfect blend of skill and athleticism. ")