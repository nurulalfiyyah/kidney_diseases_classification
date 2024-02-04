import streamlit as st
from web_functions import load_data
from Tabs import home, predict, visualize

# List of available tabs and their corresponding objects
Tabs = {
    "Home": home,
    "Prediction": predict,
    "Visualisation": visualize
}

# Create sidebar title and navigation tab list
st.sidebar.title("Navigation")
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Load data when the app starts
df, x, y = load_data()

# Checks the selected page and displays the appropriate content
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df,x,y)  # Display content with loaded data
else:
    Tabs[page].app()    # Display content without loading data