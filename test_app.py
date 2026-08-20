import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Click me"):
    st.session_state.counter += 1

st.write(f"Button clicked {st.session_state.counter} times")        

