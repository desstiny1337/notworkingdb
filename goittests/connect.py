import sqlite3
from contextlib import contextmanager

database = 'C:/Users/dess7/OneDrive/Робочий стіл/goittests/test.db'

@contextmanager
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(db_file)
    try:
        yield conn
        conn.commit()  
    except Exception as e:
        conn.rollback()  
        raise e
    finally:
        conn.close()
