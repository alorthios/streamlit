import streamlit as st
st.write('Hello World !')

st.header('st.button')

if st.button('say hello'):
    st.write('why hello')
else:
    st.write('goodbye')

print(st.button)