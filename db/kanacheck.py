from charguana import get_charset
import csv
import re
from dbhelper import Word
import sqlite3
from sqlite3 import Error
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///wordlist.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

hiragana = list(get_charset('hiragana'))
katakana = list(get_charset('katakana'))

reader_result = []
file = open('output.txt', 'w', encoding="utf8")
check = set()

with open("../words/JLPTN1.csv", "r", encoding="utf8") as word_file:
    csv_reader = csv.reader(word_file, delimiter=',')
    for row in csv_reader:
        temp_dict = {}
        for value in row:

            if not value:
                continue
            # try:
            #     check = value[0]
            # except IndexError:
            #     print(f"Row: {row}")
            match = re.findall("[/(/.\s/-a-zA-z0-9;]", value)

            alphabet_list = [c for word in match for c in word]

            if value[0] not in hiragana and value[0] not in katakana and value[0] not in alphabet_list:
                temp_dict["kanji"] = value

            elif value[0] in katakana:
                temp_dict["katakana"] = value

            elif value[0] in hiragana:
                for char in value:
                    if char not in hiragana:
                        temp_dict['kanji'] = value
                        continue
                temp_dict['hiragana'] = value

            else:
                temp_dict["meaning"] = value

        if 'katakana' in temp_dict.keys():
            word = Word(katakana=temp_dict['katakana'], meaning=temp_dict['meaning'])
            session.add(word)
            file.write(f"Katakana: {temp_dict['katakana']}, Meaning: {temp_dict['meaning']}\n")


        elif 'hiragana' in temp_dict.keys() and 'kanji' not in temp_dict.keys():
            word = Word(hiragana=temp_dict['hiragana'], meaning=temp_dict['meaning'])
            session.add(word)
            file.write(f"Hiragana: {temp_dict['hiragana']}, Meaning: {temp_dict['meaning']}\n")

        else:
            try:
                word = Word(kanji=temp_dict['kanji'],hiragana=temp_dict['hiragana'], meaning=temp_dict['meaning'])
                session.add(word)
                file.write(f"Kanji: {temp_dict['kanji']}, Hiragana: {temp_dict['hiragana']}, Meaning: {temp_dict['meaning']}\n")
            except KeyError:
                print(temp_dict)

session.commit()
file.close()
