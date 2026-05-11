import streamlit as st
import math 
st.title(":blue[Kalkulator Aritmatika]:rocket:")
st.header(":red[Aplikasi untuk menghitung operasi aritmatika]")
st.button("hasil faktorial"):
    number1 = int(st.number_input("masukkan angka 1",min_value=0, format="%0.1f"))
    if st.button("hitung"):
        hasil=math.factorial(number1)
        st.success(f"hasil {number1}!={hasil}")
    #hasil=math.sqrt(number1)
    #st.success(f"Faktorial dari {number1} adalah: **{hasil}**")
#number2 = st.number_input("masukkan angka 2")
#if st.checkbox("hasil kali"):
    #st.write(number1*number2)
#if st.checkbox("hasil bagi"):
    #st.write(number1/number2)
#st.write(
  #  "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

