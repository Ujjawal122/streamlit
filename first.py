import streamlit as st
import pandas as pd



salary=st.number_input("Enter the number")
credit=st.number_input("enter the credit score")

if salary>5000 and credit>700:
    st.write("You got the loan")
    st.balloons()
