import matplotlib.pyplot as plt
import pandas as pd
from models import EnvironmentalData, Session

def plot_aqi_overtime():
    session = Session()
    query = session.query(EnvironmentalData.date, EnvironmentalData.aqi).order_by(EnvironmentalData.date)
    df = pd.read_sql(query.statement, session.bind)

    plt.figure(figsize=(10,5))
    plt.plot(df['data'], df['aqi'], label='AQI')
    plt.title('Air Quality Index Overtime')
    plt.xlabel('Date')
    plt.ylabel('AQI')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    plot_aqi_overtime()