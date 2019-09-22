import sqlite3
from sqlite3 import Error


def get_sql_connection():
    try:
        con = sqlite3.connect('worddatabase.db')
        print("Connection is established...")

        return con

    except Error:
        print(Error)

def create_table(con, table_name, column1, column2, column3, column4):
    cursorObj = con.cursor()

    try:

        cursorObj.execute(f"""CREATE TABLE {table_name}(id integer PRIMARY KEY, {column1} text,
        {column2} text, {column3} text, {column4} text)""")

        con.commit()

    except Error:
        print("Table could not be created")
        print(Error)

con = get_sql_connection()
cursorObj = con.cursor()

[print(row) for row in cursorObj.fetchall()]

print()
con.commit()
con.close()
