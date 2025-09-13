import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import pickle


# page layout
st.set_page_config( 
            page_title = 'Employee Attrition Details',
            page_icon = 'B',
            layout='wide')


c1,c2 = st.columns([0.2,2])
c1.image('icon.jpeg')
c2.title("Employee Attrition")

def home():
    st.title("Home")
    

st.navigation([home])