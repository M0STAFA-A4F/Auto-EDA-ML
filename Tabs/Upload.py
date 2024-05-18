import streamlit as st


def upload(df):
    file = st.file_uploader('Upload file', type=['csv', 'json', 'xlsx'])

    if file is not None:
        with st.spinner('Wait for it...'):
            df.all = df.read_file(file)
        
        n_rows = st.slider('Choose number of rows to display', min_value=5, max_value=len(df.all), step=1)
        features_name = st.multiselect('Select Features to use', df.all.columns.to_list(), default=df.all.columns[:-1].to_list())
        
        df.features = df.all[features_name]
        st.write(df.features.iloc[:n_rows])
        
        target_name = st.multiselect('Select the Target', df.remainder_col(features_name, df.all.columns.to_list()), df.all.columns[-1], max_selections=1)
        
        df.target = df.all[target_name]
        st.write(df.target.iloc[:n_rows])
    