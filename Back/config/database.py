'''
  Developed by Brayan Cataño Giraldo.
  E-mail: b.catano@utp.edu.co
'''

'''
  This file contains the database configuration.
  It is used to create the database engine and the session.
  The database engine is used to connect to the database.
  The session is used to interact with the database.
'''
# Import the required libraries.
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# File name of the database and relative path.
sqlite_file_name = "../dataflor.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# Create the database engine and the session.
engine = create_engine(database_url, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()