import streamlit
import pandas
streamlit.title('Hello to Streamlit')
streamlit.header('Breakfast items')
streamlit.text('🥣 Omega')
streamlit.text('🥗 Kale')
streamlit.text('🐔 egg')
streamlit.text('🥑🍞 Avacado & toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
 
