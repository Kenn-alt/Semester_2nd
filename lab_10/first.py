import psycopg2

conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "NaruSaske51>_",
                        port = 5432)

cursor = conn.cursor()

create_table_query = '''
    CREATE TABLE people (
    person_id SERIAL NOT NULL PRIMARY KEY, 
    name varchar(255), 
    age int
    );
'''

extract_table_content_query = '''
    SELECT * FROM people;
'''

cursor.execute(extract_table_content_query)
conn.commit()
