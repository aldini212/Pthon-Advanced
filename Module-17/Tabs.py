import streamlit as st
from fontTools.ttLib.tables.T_S_I__1 import table_T_S_I__1

tab1, tab2, tab3, tab4,= st.tabs(["tab1","tab2","tab3","tab4"])

with tab1:
    st.header("Content for tab 1")
    st.write("This is the content for the 1 tab")

with tab2:
    st.header("Content for tab 2")
    st.write("This is the content for the 2 tab")

with tab3:
    st.header("Content for tab 3")
    st.write("This is the content for the 3 tab")

with tab4:
    st.header("Content for tab 4")
    st.write("This is the content for the 4 tab")