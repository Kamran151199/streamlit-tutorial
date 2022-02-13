import pandas as pd


data = pd.read_csv('cars.csv')
brands = list(data['Make'].unique())

