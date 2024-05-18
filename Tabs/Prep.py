import streamlit as st
from pycaret.classification import *
from pycaret.regression import *


def prep(df):
    train_size = st.slider('Choose train size percentage', min_value=10, max_value=100, value=70, step=1) / 100
    
    prediction_type = st.radio("Prediction Type", ['Classification', 'Regression'], index=df.prediction_type(),)
    
    if prediction_type == 'Classification':
        setup(data=df.all, target=df.target.columns[0], train_size=train_size)
       
    else:
        setup(data=df.all, target=df.target.columns[0], train_size=train_size, remove_outliers = True)
        
    
    setup_df = pull()
    st.dataframe(setup_df)
    
    best_model = compare_models()
    compare_df = pull()
    
    return best_model, compare_df