import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#Create a repeatable code block (function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

#New section to display fruityvice api advice
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

streamlit.header("The fruit load list contains:")
#Snowflake integration
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("select * from fruit_load_list as List")
       return my_cur.fetchall()

#add button to get fruit
if streamlit.button('Get fruit and list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

#dont run anything here until i fix it
streamlit.stop()

#Allows users to add fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thank you for adding: ', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
