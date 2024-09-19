from sqlalchemy import create_engine

DATABASE_URL = 'sqlite:///mydatabase.db'

engine = create_engine(DATABASE_URL)