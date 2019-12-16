import sqlite3
from sqlite3 import Error
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Word(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    hiragana = Column(String)
    katakana = Column(String)
    kanji = Column(String)
    meaning = Column(String)
    level = Column(String)

class Users(Base):
    __tablename__= 'users'

    discord_id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(String)





# ## CREATE DB ##
# def create_connection(db_file):
#     """ create a database connection to a SQLite database """
#     conn = None
#     try:
#         conn = sqlite3.connect('wordlist.db')
#         print(sqlite3.version)
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()
#
#
# if __name__ == '__main__':
#     create_connection(r"C:\sqlite\db\pythonsqlite.db")
