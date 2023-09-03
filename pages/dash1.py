import streamlit as sl

sl.sidebar.title("Navigation")
sl.sidebar.image("assets/footprint.png")

with open('style.css') as f:
    sl.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
sl.title("Hello, welcome to your **DASHBOARD**.")

sl.subheader("Three Main Factors")
col1, col2, col3 = sl.columns(3)

# Insert HTML content in col1

# Create a link in col3
col1.header("Recommend")
col1.write("Visit the [Recommendations] Page (http://localhost:8501/Dashboard)")
# Create a link in col2
col2.header("To Do")
col2.write("Visit [ToDo](https://www.google.com)")

# Create a link in col3
col3.header("Strategy")
col3.write("Visit the [Strategy] Page (http://localhost:8501/Strategy)")
