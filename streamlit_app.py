import streamlit as st

st.title("🎈 My new Strealmit app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import time 
def num_generator():
    input('Whats your name? ')
    for i in range(3):
        yield i
        time.sleep(2)

st.write_stream(num_generator)