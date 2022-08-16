"""
This file converts the raw daily data from DEFRA into weekly or monthly data.
"""
import pandas as pd
from sys import platform

def loadCSV(dataset: str, region: str):
	if platform == "linux" or platform == "linux2":
		strFormat = rf"./src/csv/{region}/{dataset}.csv"
	elif platform == "win32":
		strFormat = rf".\csv\{region}\{dataset}.csv"
	csvLoaded = pd.read_csv(strFormat)
	return csvLoaded

def prepare(region, timescale):
	if region == "LWM":
		pm25Daily = loadCSV("pm25", region)
		if timescale == "WEEKLY":
			pm25Weekly = pm25Daily
			pm25Weekly['Date'] = pd.to_datetime(pm25Weekly['Date'], infer_datetime_format=True)
			pm25Weekly['Date'] = pm25Weekly['Date'].dt.to_period("W-WED")
			pm25Weekly.rename(columns={'Date': 'Week', 'Volume (V µg/m3)': 'PM2.5 Volume'}, inplace=True)
			# print(pm25Weekly.info())
		print(pm25Weekly)
