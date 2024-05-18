import streamlit as st
import Model.DataFrame as mdf
import Tabs.Download
import Tabs.ML
import Tabs.Prep
import Tabs.Upload
import Tabs.EDA


st.header('''
          Welcome to your journey into the future of data-driven decision-making! 
          Our platform harnesses the power of auto analysis and machine learning to transform complex data into actionable insights. 
          Dive into a seamless experience where technology meets intuition, and let the algorithms pave the way to innovation. 
          Your quest for knowledge and efficiency starts here.\n
          welcome aboard 🚀
          ''')
  
upload, eda, prep, ml, download = st.tabs(["Upload", "EDA", "Preparation", "Best ML", "Download"])

df = mdf.DataFrame()

with upload:
   st.header("Upload File")
   Tabs.Upload.upload(df)

with eda:
   st.header("Exploratory Data Analysis")
   try:
       Tabs.EDA.eda(df)
   except:
       st.write("Upload file first")

with prep:
   st.header("Data Preparation")
   try:
       best_model, compare_df = Tabs.Prep.prep(df)
   except:
       st.write("Upload file first")
   
with ml:
   st.header("The Best Machine Learning Model")
   try:
       Tabs.ML.ml(compare_df)
   except:
       st.write("Upload file first")
   
with download:
   st.header("Download The Best Machine Learning Model")
   try:
       Tabs.Download.download(best_model, compare_df)
   except:
       st.write("Upload file first")
   
    
