import streamlit as st
import math 
st.title(":blue[Kalkulator Aritmatika]:rocket:")
st.header(":red[Aplikasi untuk menghitung operasi aritmatika]")
number = st.number_input("masukkan angka 1",min_value=0)
satu,dua,tiga=st.column(3)
satu=st.button("operasi faktorial")
dua=st.button("operasi akar kuadrat")
tiga=st.button("operasi kuadrat")
if satu:
    number = int(number)
    st.write(math.factorial(number))
elif dua:
    st.write(math.sqrt(number))
elif tiga :
    st.write(math.sqr(number))
           
    #hasil=math.sqrt(number1)
    #st.success(f"Faktorial dari {number1} adalah: **{hasil}**")
#number2 = st.number_input("masukkan angka 2")
#if st.checkbox("hasil kali"):
    #st.write(number1*number2)
#if st.checkbox("hasil bagi"):
    #st.write(number1/number2)
#st.write(
  #  "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

