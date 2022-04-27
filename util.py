import re
import psycopg2
from psycopg2 import Error

class CursorByName():
    def __init__(self, cursor):
        self._cursor = cursor
    
    def __iter__(self):
        return self

    def __next__(self):
        row = self._cursor.__next__()

        return { description[0]: row[col] for col, description in enumerate(self._cursor.description) }
    
# this function is based on the tutorial at: https://pynative.com/python-postgresql-tutorial/
def connect_to_db(username,password,host,port,database):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user=username,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        print("connected to the database")

        return cursor, connection

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    

def disconnect_from_db(connection,cursor):
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
    else:
        print("Connection does not work.")


# run_sql(cursor,"select from;")
def run_sql(cursor, sql_string=""):
    try:
        # Executing a SQL query
        # cursor.execute("SELECT version();")
        # cursor.execute("SELECT * from customer;")
        cursor.execute(sql_string)
    except (Exception, Error) as error:
        print("Errors while executes the code: ", error)
        return -1

# run_sql(cursor,"select from;")
def run_and_fetch_sql(cursor, sql_string=""):
    try:
        # Executing a SQL query
        # cursor.execute("SELECT version();")
        # cursor.execute("SELECT * from customer;")
        cursor.execute(sql_string)
        # Fetch result
        # record = cursor.fetchone()
        # print("You are connected to - ", record, "\n")
        record = cursor.fetchall()
        # print("Here are the first 5 rows", record[:5])
        return record
    except (Exception, Error) as error:
        print("Errors while executes the code: ", error)
        return -1


# run_sql(cursor,"select from;")
def run_and_fetch_sql_objects(cursor, sql_string=""):
    try:
        # Executing a SQL query
        # cursor.execute("SELECT version();")
        # cursor.execute("SELECT * from customer;")
        cursor.execute(sql_string)
        # Fetch result
        # record = cursor.fetchone()
        # print("You are connected to - ", record, "\n")
        #record = cursor.fetchall()
        # print("Here are the first 5 rows", record[:5])
        records = '['
        for row in CursorByName(cursor):
            records = records + str(row).replace('\'','"') + ','
        records = records[:-1] + ']'

        if(records == ']'):
            records ='[]'
        return records
    except (Exception, Error) as error:
        print("Errors while executes the code: ", error)
        return -1