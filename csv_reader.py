import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
engine = create_engine('postgresql://postgres:postgres@localhost/postgres')
db = scoped_session(sessionmaker(bind=engine))

f = open('flights.csv')
reader = csv.reader(f)

for origin, destination, duration in reader:
    db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
               {"origin": origin, "destination": destination, "duration": duration})
    print(f"Added {origin} to {destination}")
db.commit()
