import streamlit as st
import numpy as np
import pandas as pd
import json
from scrape2 import get_prerequisite_text, get_course_title, html_content


def show_courses(filepath:str):
  with open(filepath, 'r') as f:
    data = json.load(f)

  df = pd.json_normalize(data['courses'],
                         meta=['code', 'title', 'prerequisites'])
  
  #df.columns = ['Code', 'Name', 'Prerequisites']

  df


st.title('Mathematics Courses at UTM')

show_courses('courses.json')

# Add select box to select campus, automatically add H5
st.markdown("## _I want to know the prerequisites for a course._")
course_inputted = st.text_input('Course code:')  
st.write("")
st.markdown(f"**{get_course_title(course_inputted)}**")
st.markdown(get_prerequisite_text(course_inputted))
