from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta
import os

DATABASE_URL = os.getenv("url")
engin = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engin)

Base: DeclarativeMeta = declarative_base()
