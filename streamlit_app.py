import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
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
