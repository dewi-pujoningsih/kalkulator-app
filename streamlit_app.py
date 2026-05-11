import streamlit as st
import math 
st.title(":blue[Kalkulator Aritmatika]:rocket:")
st.header(":red[Aplikasi untuk menghitung operasi aritmatika]")
number = st.number_input("masukkan angka 1",min_value=0)
satu,dua,tiga=st.columns(3)
#satu=st.button("operasi faktorial")
#dua=st.button("operasi akar kuadrat")
#tiga=st.button("operasi kuadrat")
if satu.button("operasi faktorial"):
    number = int(number)
    st.write(math.factorial(number))
elif dua.button("operasi akar kuadrat"):
    st.write(math.sqrt(number))
elif tiga.button("operasi kuadrat") :
    st.write(number**2)
if st.button("reset"):
    st.rerun()
   
