"""
This file converts the raw daily data from DEFRA into weekly or monthly data.
"""
from sys import platform
import pandas as pd
import graph

def loadCSV(dataset: str, region: str):
	if platform == "linux" or platform == "linux2":
		strFormat = rf"./src/csv/{region}/{dataset}.csv" # Todo: allow main.py to be run from anywhere not just src/main.py
	elif platform == "win32":
		strFormat = rf".\csv\{region}\{dataset}.csv"
	csvLoaded = pd.read_csv(strFormat)
	return csvLoaded

def prepare(region, timescale):
	if region == "LWM":
		pm25Daily = loadCSV("pm25", region)
		nitroDioxideDaily = loadCSV("nitrogenDioxide", region)
		if timescale == "WEEKLY":
			pm25Weekly = pm25Daily
			pm25Weekly['Date'] = pd.to_datetime(pm25Weekly['Date'], infer_datetime_format=True)
			pm25Weekly['Date'] = pm25Weekly['Date'].dt.to_period("W-WED").dt.end_time.dt.strftime("%Y-%m-%d")
			pm25Weekly.rename(columns={'Date': 'Week', 'Volume (V µg/m3)': 'PM2.5 Volume'}, inplace=True)

			nitroDioxideWeekly = nitroDioxideDaily
			nitroDioxideWeekly['Date'] = pd.to_datetime(nitroDioxideWeekly['Date'], infer_datetime_format=True)
			nitroDioxideWeekly['Date'] = nitroDioxideWeekly['Date'].dt.to_period("W-WED").dt.end_time.dt.strftime("%Y-%m-%d")
			nitroDioxideWeekly.rename(columns={'Date': 'Week', 'Volume (V µg/m3)': 'Nitrogen Dioxide Volume'}, inplace=True)

			LWMWeekly = pd.merge(pm25Weekly, nitroDioxideWeekly)
			#print(LWMWeekly)

			graph.generateGraph("LWM", LWMWeekly, timescale)
		if timescale == "MONTHLY":
			pm25Monthly = pm25Daily
			pm25Monthly['Date'] = pd.to_datetime(pm25Monthly['Date'], infer_datetime_format=True)
			pm25Monthly['Date'] = pm25Monthly['Date'].dt.to_period("M").dt.end_time.dt.strftime("%Y-%m")
			pm25Monthly.rename(columns={'Date': 'Month', 'Volume (V µg/m3)': 'PM2.5 Volume'}, inplace=True)

			nitroDioxideMonthly = nitroDioxideDaily
			nitroDioxideMonthly['Date'] = pd.to_datetime(nitroDioxideMonthly['Date'], infer_datetime_format=True)
			nitroDioxideMonthly['Date'] = nitroDioxideMonthly['Date'].dt.to_period("M").dt.end_time.dt.strftime("%Y-%m")
			nitroDioxideMonthly.rename(columns={'Date': 'Month', 'Volume (V µg/m3)': 'Nitrogen Dioxide Volume'}, inplace=True)

			#print(nitroDioxideMonthly)

			LWMMonthly = pd.merge(pm25Monthly, nitroDioxideMonthly)
			#print(LWMMonthly)
			
			graph.generateGraph("LWM", LWMMonthly, timescale)
