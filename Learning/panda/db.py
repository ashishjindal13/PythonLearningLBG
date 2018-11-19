# pip install --only-binary :all: mysqlclient
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

con = sa.create_engine('mysql+mysqldb://root:sasa@127.0.0.1:3306/docker_mysql_01')

def copytable(tableName):
    chunks = pd.read_csv('../data/' + tableName+'.csv', chunksize=100000)
    for chunk in chunks:
        chunk.to_sql(name=tableName, if_exists='append', con=con)

# copytable('airports')
Base = declarative_base()

class State (Base):
    __tablename__ = 'airports'
    index = Column(Integer, primary_key=True)
    IATA_CODE = Column(String(16))

Session = sessionmaker(bind=con)
sesh = Session()
q=sesh.query(State).filter(State.IATA_CODE=='ABE').one()
print(q)
print(q.index,q.IATA_CODE)