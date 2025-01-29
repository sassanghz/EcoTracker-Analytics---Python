import pandas as pd
from sqlalchemy.orm import sessionmaker
from models import EnvironmentalData, engine

Session = sessionmaker(bind=engine)
session = Session()

def load_date():
    file_path = 'environmental_data.csv'
    data = pd.read_csv(file_path)

    for index, row in data.iterrows():
        data_point = EnvironmentalData(
            date = pd.to_datetime(row['Date']),
            location = row['location'],
            aqi = row['AQI']
        )

        session.add(data_point)
    session.commit()

if __name__ == '__main__':
    load_date()

