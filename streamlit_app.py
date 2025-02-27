import streamlit as st
st.title(":blue[Kalkulator Aritmatika]")
number1 = st.number_input("masukkan angka 1")
number2 = st.number_input("masukkan angka 2")
if st.button("Hasil kali", type="primary"):
    st.write(number1*number2)
elif if st.button("Hasil bagi", type="primary"):
    st.write(number1/number2)
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
