# a database model for the environmental data
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class EnvironmentalData(Base):
    __tablename__ = 'environmental_data'
    id = Column(Integer, primary_key = True)
    date = Column(Date)
    location = Column(String)
    aqi = Column(float) #index for air quality


#DB setup
engine = create_engine('sqlite:///environment_data.db')
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    init_db()

# the environmental data is stored in a database
# this initilizes the data