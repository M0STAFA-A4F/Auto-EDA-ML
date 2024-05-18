from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


def eda(df):
    profile_report = ProfileReport(df.all)
    st_profile_report(profile_report)
    