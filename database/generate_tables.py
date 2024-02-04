
from database.database import engine, Base


def generate_tables():
    Base.metadata.create_all(bind=engine)
