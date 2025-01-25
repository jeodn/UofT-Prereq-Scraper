import streamlit as st
import numpy as np
import pandas as pd
from scrape_utm import get_prerequisites

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

st.write('hello')

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
st.selectbox('cuck', ['a', 'b', 'c'])

add_selectbox = st.sidebar.selectbox('yes', ('a', 'b', 'c'))

course_inputted = st.text_input('Course code')
st.write(get_prerequisites(course_inputted))
