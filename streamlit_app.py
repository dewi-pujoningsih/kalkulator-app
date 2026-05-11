import streamlit as st
import math 
st.title(":blue[Kalkulator Aritmatika]:rocket:")
st.header(":red[Aplikasi untuk menghitung operasi aritmatika]")
number = st.number_input("masukkan angka=",min_value=0)
satu,dua,tiga=st.columns(3)
empat,lima=st.columns(2)
satu=st.button("operasi faktorial")
dua=st.button("operasi akar kuadrat")
tiga=st.button("operasi kuadrat")
empat=st.button("operasi logaritma")
lima=st.button("operasi ln")
if satu:
    number = int(number)
    st.write(math.factorial(number))
elif dua:
    st.write(math.sqrt(number))
elif tiga :
    st.write(number**2)
elif empat :
    st.write(math.log(number))
elif lima:
    st.write(math.ln(number))
if st.button("reset"):
    st.rerun()
   
