from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL = "postgresql://student:password@localhost/club?options=-csearch_path%3Ddbo,cd"
URL = 'postgresql://student:P56IkyXWteEb@ep-old-forest-a257c2xq.eu-central-1.aws.neon.tech/club?sslmode=require'
engine = create_engine(URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()