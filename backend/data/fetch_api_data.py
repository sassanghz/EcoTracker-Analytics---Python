#script for fetching data from existing APIS and saving it as a csv
import requests
import pandas as pd

def fetch_data_and_save():
    #API Endpoint
    url = 'https://www.epa.gov/outdoor-air-quality-data'
    params = {'apikey': 'YourAPIKey', 'other_params': 'values'}

    response = requests.get(url, params=params)
    data = response.json()

    # Convert JSON data to DataFrame
    df = pd.DataFrame(data)
    
    # Optional: Process or clean data
    df['date'] = pd.to_datetime(df['date'])  # Example of data cleaning

    # Save to CSV
    df.to_csv('C:\Users\sassa\Documents\EcoTracker\backend\data\environmental_data.csv', index=False)

if __name__ == '__main__':
    fetch_data_and_save()
