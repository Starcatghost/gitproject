import sqlite3

DB_NAME = 'MoviesAoiInfo.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.close()

# init_db() 

def create_table(DB_NAME, table_name = 'MoviesData'):
    query = f''' CREATE TABLE IF NOT EXISTS {table_name}
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT,
              year INTEGER,
              imdb_rating REAL,
              genres TEXT,
              poster TEXT
              )
              '''
    


    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

# create_table(DB_NAME, 'MovieData')

def insert_record( title , year , imdb_rating , genres ,poster):
    query = f'''INSERT INTO MovieData (title , year , imdb_rating , genres , poster)
    VALUES(? , ?, ?, ?, ?)
    '''

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()   
    cursor.execute(query, (title , year , imdb_rating , genres ,poster))
    conn.commit()
    conn.close()

# insert_record('Inception', 2001, 7.8,'Action , Drama', 'http://test.com')

def insert_list_of_movies(movies_list):
    conn = sqlite3.connect(DB_NAME)
    for item in movies_list:
        
            title =item['title']
            year = item['year']
            imdb_rating = item['imdb_rating']
            genres = ','.join(item['genres'])
            poster = item['poster']
            insert_record(title , year , imdb_rating , genres ,poster)

    return f'{len(movies_list)} Record Inserted Sucessfully'                    


# movies_list = [{'title':'God father' , 'year' : '2020' , 'imdb_rating' : '8.5' , 
#                 'genres' : 'Action , Drama' , 'poster' : 'https://test1.com'},
#                 {'title':'Dark knight' , 'year' : '2004' , 'imdb_rating' : '6.3' , 
#                  'genres' : 'Action , Mystry' , 'poster' : 'https://test2.com'}]

# print(insert_list_of_movies(movies_list))