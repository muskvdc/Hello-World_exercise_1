import streamlit as st

st.title('Hello, World! 🌍')
st.write('My first deployed Streamlit app!')

name = st.text_input('Your name:')
if name:
    st.success(f'Hello, {name}!')