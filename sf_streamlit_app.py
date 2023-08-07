import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.divider()
streamlit.text('🥣 Oatmeal and Almond Milk')
streamlit.divider()
streamlit.text('🐔 Non-pork Bacon and Synth-Eggs')
streamlit.divider()
streamlit.text('🥗 Tossed Vegatables')
streamlit.divider()
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
