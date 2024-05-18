import streamlit as st
from pycaret.classification import *
from pycaret.regression import *


def download(best_model, compare_df):
    best_model = st.selectbox('Select Model', compare_df)
    
    save_model(best_model, 'best_model')
    
    with open('best_model.pkl', 'rb') as f:
        st.download_button('Download the Model', f, 'trained_model.pkl')