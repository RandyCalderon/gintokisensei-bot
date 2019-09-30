import sqlalchemy as db

connection_string = 'sqlite:///worddatabase.db'
engine = db.create_engine(connection_string)
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('JLPTN1', metadata, autoload=True, autoload_with=engine)

# Print the column names
print(census.columns.keys())
