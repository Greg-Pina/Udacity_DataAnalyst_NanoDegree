import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return conn, cur


def drop_tables(conn, cur):
    """
    Drops each table using the queries in `drop_table_queries` list.
    
    Parameters:
        conn: psycopg2 connection object
        cur: psycopg2 cursor object
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(conn, cur):
    """
    Creates each table using the queries in `create_table_queries` list.
    
    Parameters:
        conn: psycopg2 connection object
        cur: psycopg2 cursor object
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database.
    
    - Establishes connection with the sparkify database and gets
      a cursor to it.
    
    - Drops all the tables.
    
    - Creates all tables needed.
    
    - Finally, closes the connection.
    """
    # Create sparkifydb and get connection + cursor
    conn, cur = create_database()
    
    # Drop all existing tables
    drop_tables(conn, cur)
    
    # Create all necessary tables
    create_tables(conn, cur)

    # Close connection
    conn.close()


if __name__ == "__main__":
    main()
