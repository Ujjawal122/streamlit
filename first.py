import streamlit as st
import pandas as pd

st.title('Dat analysis app')

df=pd.read_csv(r'C:\Users\vipin kumar\Desktop\Data Science\springBoot\titanic (1).csv')
df

salary=st.number_input("Enter the number")
credit=st.number_input("enter the credit score")

if salary>5000 and credit>700:
    st.write("You got the loan")
    st.balloons()