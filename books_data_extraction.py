import requests
import mysql.connector

API_KEY = 'AIzaSyC0GRLZpJHyTDOtN9iB3YmSc_8QN0OjWyU'

def get_books_data(search_query):
    url = f'https://www.googleapis.com/books/v1/volumes?q={search_query}&key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data['items'] if 'items' in data else []

def insert_books_data(data):
    connection = mysql.connector.connect(
        host="localhost",  # or the host of your database
        user="root",       # your MySQL username
        password="Tamil@123456", # your MySQL password
        database="bookscape_db"
    )
    cursor = connection.cursor()
    for item in data:
        book_info = item['volumeInfo']
        cursor.execute('''
            INSERT INTO books (book_id, search_key, book_title, book_subtitle, book_authors,
            book_description, industryIdentifiers, text_readingModes, image_readingModes, pageCount,
            categories, language, imageLinks, ratingsCount, averageRating, country, saleability,
            isEbook, amount_listPrice, currencyCode_listPrice, amount_retailPrice, currencyCode_retailPrice,
            buyLink, year)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            item['id'],
            search_query,
            book_info.get('title', ''),
            book_info.get('subtitle', ''),
            ', '.join(book_info.get('authors', [])),
            book_info.get('description', ''),
            str(book_info.get('industryIdentifiers', [])),
            book_info.get('readingModes', {}).get('text', False),
            book_info.get('readingModes', {}).get('image', False),
            book_info.get('pageCount', 0),
            ', '.join(book_info.get('categories', [])),
            book_info.get('language', ''),
            str(book_info.get('imageLinks', {})),
            book_info.get('ratingsCount', 0),
            book_info.get('averageRating', 0),
            book_info.get('country', ''),
            book_info.get('saleability', ''),
            book_info.get('isEbook', False),
            book_info.get('listPrice', {}).get('amount', 0),
            book_info.get('listPrice', {}).get('currencyCode', ''),
            book_info.get('retailPrice', {}).get('amount', 0),
            book_info.get('retailPrice', {}).get('currencyCode', ''),
            book_info.get('buyLink', ''),
            book_info.get('publishedDate', '').split('-')[0]  # Extract the year
        ))
    connection.commit()
    cursor.close()
    connection.close()
import requests

# Define the search_query variable (you can change this to the user's search input or a preset query)
search_query = "python programming"  # Example search query

# Google Books API URL
url = "https://www.googleapis.com/books/v1/volumes?q=" + search_query

# Send request to the API
response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:
    # Parse the response JSON
    data = response.json()
    # Print the first book title as an example
    if "items" in data:
        book = data["items"][0]["volumeInfo"]
        print("Title: ", book.get("title"))
else:
    print(f"Error {response.status_code}: Unable to fetch data.")
