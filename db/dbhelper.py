from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import MetaData
import csv
from charguana import get_charset

Base = declarative_base()
engine = create_engine('sqlite:///wordlist.db')
# Session = sessionmaker(bind=engine)
# session = Session()

def get_db_information(engine):
    m = MetaData()
    m.reflect(engine)
    for table in m.tables.values():
        print(table.name)
        for column in table.c:
            print(column.name)

def import_word_data(filename):

    # Read Hiragana/Kanji csv file
    # Each row is stored as a list
    # For the first two items in the list perform a check
        # IF the ALL the characters of the current item in the list we're looking at do not belong
        # to the hiragana character set
        # THEN it is kanji and label it as such

    # Read Katakana/Hiragana csv file
        # For the first two items in the list perform a check
            # IF the ALL the characters of the current item in the list we're looking at do not belong
            # to the katakana character set
            # THEN it is hiragana and label it as such

    with open(filename, encoding='utf8') as word_file:
        csv_reader = csv.reader(word_file, delimiter='~')
        count = 0
        for row in csv_reader:
            count +=1
            print(row)
        print(count)
            # for item in row:
            #     if 'arab' in item:
            #         print(row)


import_word_data(r'C:\Users\mishr\Documents\Gintoki Sensei Bot\gintokisensei-bot\words\JLPTN1Katakana.csv')
# class Word(Base):
#
#     __tablename__='words'
#
#     id = Column(Integer, primary_key=True)
#     hiragana = Column(String)
#     katakana = Column(String)
#     kanji = Column(String)
#     resource = Column(String)
#     label = Column(String)
#
#
# if __name__ == '__main__':
#     # Create database
#     # create_connection(r"wordlist.db")
#     Base.metadata.create_all(engine)
