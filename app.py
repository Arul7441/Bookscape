import streamlit as st
import pandas as pd
import mysql.connector

def query_db(query):
    connection = mysql.connector.connect(
        host="localhost",  # or the host of your database
        user="root",       # your MySQL username
        password="Tamil@123456", # your MySQL password
        database="bookscape_db"
    )
    df = pd.read_sql(query, connection)
    connection.close()
    return df

def display_books():
    st.title('BookScape Explorer')
    search_query = st.text_input('Search for Books:')
    if search_query:
        books = query_db(f"SELECT * FROM books WHERE book_title LIKE '%{search_query}%'")
        st.write(books)

if __name__ == '__main__':
    display_books()
