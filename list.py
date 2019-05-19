from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
engine = create_engine('postgresql://postgres:postgres@localhost/postgres')
db = scoped_session(sessionmaker(bind=engine))

flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
for flight in flights:
    print(f"Flight from {flight.origin} to {flight.destination} ({flight.duration} mins)")
