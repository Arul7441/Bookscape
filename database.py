import mysql.connector

def get_connection():
    # Update with your MySQL database credentials
    connection = mysql.connector.connect(
        host="localhost",  # or the host of your database
        user="root",       # your MySQL username
        password="Tamil@123456", # your MySQL password
        database="bookscape_db"
    )
    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id VARCHAR(255) PRIMARY KEY,
            search_key VARCHAR(255),
            book_title VARCHAR(255),
            book_subtitle TEXT,
            book_authors TEXT,
            book_description TEXT,
            industryIdentifiers TEXT,
            text_readingModes BOOLEAN,
            image_readingModes BOOLEAN,
            pageCount INT,
            categories TEXT,
            language VARCHAR(10),
            imageLinks TEXT,
            ratingsCount INT,
            averageRating DECIMAL,
            country VARCHAR(10),
            saleability VARCHAR(50),
            isEbook BOOLEAN,
            amount_listPrice DECIMAL,
            currencyCode_listPrice VARCHAR(10),
            amount_retailPrice DECIMAL,
            currencyCode_retailPrice VARCHAR(10),
            buyLink TEXT,
            year TEXT
        )
    ''')
    connection.commit()
    cursor.close()
    connection.close()
