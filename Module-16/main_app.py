import streamlit as st

if st.button("Click Me"):
    st.write("Button Clicked")



if st.checkbox("check me to show some text"):
    st.write("You're seeing this text becouse you checked the checkbox")

user_input = st.text_input("Enter Text","Simple text")
st.write("You entered:",user_input)

age = st.number_input('enter Your age',min_value=0, max_value=100)
st.write("Your age is:",age)

message = st.text_area("Enter message")
st.write("Your message:", message)


choice = st.radio("Pick one", ["HTML ","CSS","PYTHON"])
st.write('Your choice is:',choice)

try:
    7/3.5
except Exception as e:
    st.exception(e)