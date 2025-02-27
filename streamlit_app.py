import streamlit as st
pip install st-annotated-text
from annotated_text import annotated_text
annotated_text(
    "This ",
    ("is", "verb")
)
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
