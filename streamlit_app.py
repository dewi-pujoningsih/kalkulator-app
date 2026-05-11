import streamlit as st
import math 
st.title(":blue[Kalkulator Aritmatika]:rocket:")
st.header(":red[Aplikasi untuk menghitung operasi aritmatika]")
number = st.number_input("masukkan angka=",min_value=0)
satu,dua,tiga,empat,lima=st.columns(5)
if satu.button("operasi faktorial"):
    number = int(number)
    st.write(math.factorial(number))
elif dua.button("operasi akar kuadrat"):
    st.write(math.sqrt(number))
elif tiga.button("operasi kuadrat") :
    st.write(number**2)
elif empat.button("operasi logaritma") :
    st.write(math.log(number))
elif lima.button("operasi ln"):
    st.write(math.ln(number))
if st.button("reset"):
    st.rerun()
   
