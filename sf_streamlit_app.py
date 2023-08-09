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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice api advice
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json()) #just writes data onscreen

# normalize json from response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display normalized json as dataframe
streamlit.dataframe(fruityvice_normalized)
