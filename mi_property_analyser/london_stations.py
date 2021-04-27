import pandas as pd
import os


def load_london_stations():
    filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data/london_stations.csv')

    return pd.read_csv(filepath)
