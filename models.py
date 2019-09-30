from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from test import Base, engine


class WordModel(Base):
    # instances = 0

    # def __init__(self):
    #     instances += 1
    __tablename__ = 'JLPTN1'
    uuid = Column('id', Integer, primary_key=True)
    hiragana = Column('Hiragana', String(100))
    meaning = Column('Meaning', String(100))
    kanji = Column('Kanji', String(100))
    resource = Column('Resource', String(100))


Base.prepare(engine)
