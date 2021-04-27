import pandas as pd
import os


def load_london_stations():
	"""This CSV file has been downloaded from this link
	https://www.doogal.co.uk/london_stations.php """

	filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data/london_stations.csv')

	return pd.read_csv(filepath)
