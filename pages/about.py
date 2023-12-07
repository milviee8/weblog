from PIL import Image
import requests

import streamlit as st

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

st.title("Personal Background ˗ˏˋ ★ ˎˊ˗")


import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20fcfjwiyb.json")
img_contact_form = Image.open("images/me.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 1))
with image_column:
    st.image(img_contact_form)
    
with st.container():
 st.write("I graduated at Cagdianao National High School with a focus on Technical, Vocational Livelihood, specializing in the Information and Communication Technology strand, my journey reflects simplicity amidst the intricate landscapes of life. Navigating the realms of technology and vocational skills has not only enriched my academic pursuits but also shaped my perspective on leading a peaceful existence. Embracing the ethos of simplicity, I find solace in the straightforward joys of life – be it the hum of a computer or the practicality of vocational skills. The pursuit of knowledge in the realm of Information and Communication Technology has become a harmonious thread in the fabric of my uncomplicated, yet fulfilling, daily routine. Living a peaceful life, for me, transcends the complexities of the modern world. It's about finding contentment in the simplicity of routine, in the quiet moments of reflection, and in the balance struck between technology and the serenity of a tranquil existence. The skills acquired during my academic journey have not only equipped me for a future in the dynamic field of ICT but have also instilled a sense of calmness, emphasizing the beauty of leading a life that values simplicity in a world often defined by its intricacies.")
