import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from streamlit_pandas_profiling import st_profile_report
# import pandas_profiling

# st.header('st.button')

# if st.button('Say hello'):
#     st.write('Why hello there')
# else:
#     st.write('Goodbye')
# st.write('Hello world')

st.header('st.write')

st.subheader('Display text')
st.write('Hello, *World!* 🚀')

st.subheader('Display numbers')
st.write(1234)

st.subheader('Display DataFrame')
dtserver = pd.read_csv('DTserver_WWJ.csv')
st.write(dtserver)

df_basic = pd.DataFrame({
'first column': [1, 2, 3, 4],
'second column': [10, 20, 30, 40]
})



df_random = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df_random).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

# st.write('Below is a DataFrame:', df_random, 'Above is a DataFrame.')

st.write(c)

# Show a line Chart

st.header('Line chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.header('st.selectbox')

option = st.selectbox(
'What is your favorite color?',
('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)

st.header('st.multiselect')

options = st.multiselect(
'What are your favorite colors?',
['Green', 'Yellow', 'Red', 'Blue'],
['Yellow', 'Red'])

st.write('You selected:', options)

st.header('st.checkbox')

st.write('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
champagne = st.checkbox('Champagne')

if icecream:
    st.write("Great! Here's some more 🍨 ")
if coffee:
    st.write("Okay, here's some coffee ☕")
if cola:
    st.write("Here you go 🍹")
if champagne:
    st.write("Please enjoy your :champagne:")

# st.header('`streamlit_pandas_profiling`')

# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
#
# pr = df.profile_report()
#
# st_profile_report(pr)

st.header('`st.latex`')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
