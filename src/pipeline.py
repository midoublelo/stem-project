"""
This file converts the raw daily data from DEFRA into weekly or monthly data.
"""
from sys import platform
from functools import reduce
import pandas as pd
import graph

def loadCSV(dataset: str, region: str):
	if platform == "linux" or platform == "linux2":
		strFormat = rf"./src/csv/{region}/{dataset}.csv" # Todo: allow main.py to be run from anywhere not just src/main.py
	elif platform == "win32":
		strFormat = rf".\csv\{region}\{dataset}.csv"
	csvLoaded = pd.read_csv(strFormat)
	return csvLoaded

def prepare(region, timescale, mode):
	if region == "LWM": # The user's selected region
		pm25Daily = loadCSV("pm25", region) # Loads all of the CSV data available for this region
		nitroDioxideDaily = loadCSV("nitrogenDioxide", region) # Loads all of the CSV data available for this region
		if timescale == "WEEKLY": # The user's selected timescale
			pm25Weekly = pm25Daily # Create a new variable for the weekly data
			pm25Weekly['Date'] = pd.to_datetime(pm25Weekly['Date'], infer_datetime_format=True) # Create a pandas DateTime object
			pm25Weekly['Date'] = pm25Weekly['Date'].dt.to_period("W-WED").dt.end_time.dt.strftime("%Y-%m-%d") # Convert from daily to weekly
			pm25Weekly.rename(columns={'Date': 'Week', 'Volume (V µg/m3)': 'PM2.5 Volume'}, inplace=True) # Rename columns to more fitting names

			nitroDioxideWeekly = nitroDioxideDaily
			nitroDioxideWeekly['Date'] = pd.to_datetime(nitroDioxideWeekly['Date'], infer_datetime_format=True)
			nitroDioxideWeekly['Date'] = nitroDioxideWeekly['Date'].dt.to_period("W-WED").dt.end_time.dt.strftime("%Y-%m-%d")
			nitroDioxideWeekly.rename(columns={'Date': 'Week', 'Volume (V µg/m3)': 'Nitrogen Dioxide Volume'}, inplace=True)

			LWMWeekly = pd.merge(pm25Weekly, nitroDioxideWeekly) # Create a singular pandas DataFrame from both objects
			#print(LWMWeekly)

			graph.generateGraph("LWM", LWMWeekly, timescale, mode) # Generate a graph for the 'LWM' region using the merged data and user's
			# chosen timescale and output mode
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
			
			graph.generateGraph("LWM", LWMMonthly, timescale, mode)
	if region == "NCC":
		ozoneDaily = loadCSV("ozone", region)
		pm10Daily = loadCSV("pm10", region)
		pm25Daily = loadCSV("pm25", region)
		nitroDioxideDaily = loadCSV("nitrogenDioxide", region)
		print(ozoneDaily)
		if timescale == "WEEKLY":
			ozoneWeekly = ozoneDaily
			ozoneWeekly['Date'] = pd.to_datetime(ozoneWeekly['Date'], infer_datetime_format=True)
			ozoneWeekly['Date'] = ozoneWeekly['Date'].dt.to_period("W-WED").dt.end_time.dt.strftime("%Y-%m-%d")
			ozoneWeekly.rename(columns={'Date': 'Week', 'Volume(V µg/m3)': 'Ozone Volume'}, inplace=True)

			# pm10Weekly = pm10Daily
			# pm10Weekly['Date'] = pd.to_datetime(pm10Weekly['Date'], infer_datetime_format=True)
			# pm10Weekly['Date'] = pm10Weekly['Date'].dt.to_period("W-WED").dt.end_time.dt.strftime("%Y-%m-%d")
			# pm10Weekly.rename(columns={'Date': 'Week', 'Volume(V µg/m3)': 'PM10 Volume'}, inplace=True)

			pm25Weekly = pm25Daily
			pm25Weekly['Date'] = pd.to_datetime(pm25Weekly['Date'], infer_datetime_format=True)
			pm25Weekly['Date'] = pm25Weekly['Date'].dt.to_period("W-WED").dt.end_time.dt.strftime("%Y-%m-%d")
			pm25Weekly.rename(columns={'Date': 'Week', 'Volume(V µg/m3)': 'PM2.5 Volume'}, inplace=True)

			nitroDioxideWeekly = nitroDioxideDaily
			nitroDioxideWeekly['Date'] = pd.to_datetime(nitroDioxideWeekly['Date'], infer_datetime_format=True)
			nitroDioxideWeekly['Date'] = nitroDioxideWeekly['Date'].dt.to_period("W-WED").dt.end_time.dt.strftime("%Y-%m-%d")
			nitroDioxideWeekly.rename(columns={'Date': 'Week', 'Volume(V µg/m3)': 'Nitrogen Dioxide Volume'}, inplace=True)

			multiData = [ozoneWeekly, pm25Weekly, nitroDioxideWeekly] # [ozoneWeekly, pm10Weekly, pm25Weekly, nitroDioxideWeekly]
			NCCWeekly = reduce(lambda left, right: pd.merge(left, right, on='Week'), multiData)
			print(NCCWeekly)

			graph.generateGraph("NCC", NCCWeekly, timescale, mode)
		if timescale == "MONTHLY":
			ozoneMonthly = ozoneDaily
			ozoneMonthly['Date'] = pd.to_datetime(ozoneMonthly['Date'], infer_datetime_format=True)
			ozoneMonthly['Date'] = ozoneMonthly['Date'].dt.to_period("M").dt.end_time.dt.strftime("%Y-%m")
			ozoneMonthly.rename(columns={'Date': 'Month', 'Volume(V µg/m3)': 'Ozone Volume'}, inplace=True)

			# pm10Monthly = pm10Daily
			# pm10Monthly['Date'] = pd.to_datetime(pm10Monthly['Date'], infer_datetime_format=True)
			# pm10Monthly['Date'] = pm10Monthly['Date'].dt.to_period("M").dt.end_time.dt.strftime("%Y-%m")
			# pm10Monthly.rename(columns={'Date': 'Month', 'Volume(V µg/m3)': 'PM10 Volume'}, inplace=True)

			pm25Monthly = pm25Daily
			pm25Monthly['Date'] = pd.to_datetime(pm25Monthly['Date'], infer_datetime_format=True)
			pm25Monthly['Date'] = pm25Monthly['Date'].dt.to_period("M").dt.end_time.dt.strftime("%Y-%m")
			pm25Monthly.rename(columns={'Date': 'Month', 'Volume(V µg/m3)': 'PM2.5 Volume'}, inplace=True)

			nitroDioxideMonthly = nitroDioxideDaily
			nitroDioxideMonthly['Date'] = pd.to_datetime(nitroDioxideMonthly['Date'], infer_datetime_format=True)
			nitroDioxideMonthly['Date'] = nitroDioxideMonthly['Date'].dt.to_period("M").dt.end_time.dt.strftime("%Y-%m")
			nitroDioxideMonthly.rename(columns={'Date': 'Month', 'Volume(V µg/m3)': 'Nitrogen Dioxide Volume'}, inplace=True)

			#print(nitroDioxideMonthly)
			ozoneMonthly.drop_duplicates(subset='Month')
			pm25Monthly.drop_duplicates(subset='Month')
			nitroDioxideMonthly.drop_duplicates(subset='Month')
			multiData = [ozoneMonthly, pm25Monthly, nitroDioxideMonthly] # [ozoneMonthly, pm10Monthly, pm25Monthly, nitroDioxideMonthly]
			NCCMonthly = reduce(lambda left, right: pd.merge(left, right, on='Month', how='left'), multiData)
			print(NCCMonthly)
			
			graph.generateGraph("NCC", NCCMonthly, timescale, mode)
	if region == "LEC":
		ozoneDaily = loadCSV("ozone", region)
		#pm10Daily = loadCSV("pm10", region)
		pm25Daily = loadCSV("pm25", region)
		nitroDioxideDaily = loadCSV("nitrogenDioxide", region)
		print(ozoneDaily)
		if timescale == "WEEKLY":
			ozoneWeekly = ozoneDaily
			ozoneWeekly['Date'] = pd.to_datetime(ozoneWeekly['Date'], infer_datetime_format=True)
			ozoneWeekly['Date'] = ozoneWeekly['Date'].dt.to_period("W-WED").dt.end_time.dt.strftime("%Y-%m-%d")
			ozoneWeekly.rename(columns={'Date': 'Week', 'Volume(V µg/m3)': 'Ozone Volume'}, inplace=True)

			# pm10Weekly = pm10Daily
			# pm10Weekly['Date'] = pd.to_datetime(pm10Weekly['Date'], infer_datetime_format=True)
			# pm10Weekly['Date'] = pm10Weekly['Date'].dt.to_period("W-WED").dt.end_time.dt.strftime("%Y-%m-%d")
			# pm10Weekly.rename(columns={'Date': 'Week', 'Volume(V µg/m3)': 'PM10 Volume'}, inplace=True)

			pm25Weekly = pm25Daily
			pm25Weekly['Date'] = pd.to_datetime(pm25Weekly['Date'], infer_datetime_format=True)
			pm25Weekly['Date'] = pm25Weekly['Date'].dt.to_period("W-WED").dt.end_time.dt.strftime("%Y-%m-%d")
			pm25Weekly.rename(columns={'Date': 'Week', 'Volume(V µg/m3)': 'PM2.5 Volume'}, inplace=True)

			nitroDioxideWeekly = nitroDioxideDaily
			nitroDioxideWeekly['Date'] = pd.to_datetime(nitroDioxideWeekly['Date'], infer_datetime_format=True)
			nitroDioxideWeekly['Date'] = nitroDioxideWeekly['Date'].dt.to_period("W-WED").dt.end_time.dt.strftime("%Y-%m-%d")
			nitroDioxideWeekly.rename(columns={'Date': 'Week', 'Volume(V µg/m3)': 'Nitrogen Dioxide Volume'}, inplace=True)

			multiData = [ozoneWeekly, pm25Weekly, nitroDioxideWeekly] # [ozoneWeekly, pm10Weekly, pm25Weekly, nitroDioxideWeekly]
			LECWeekly = reduce(lambda left, right: pd.merge(left, right, on='Week'), multiData)
			print(LECWeekly)

			graph.generateGraph("LEC", LECWeekly, timescale, mode)
		if timescale == "MONTHLY":
			ozoneMonthly = ozoneDaily
			ozoneMonthly['Date'] = pd.to_datetime(ozoneMonthly['Date'], infer_datetime_format=True)
			ozoneMonthly['Date'] = ozoneMonthly['Date'].dt.to_period("M").dt.end_time.dt.strftime("%Y-%m")
			ozoneMonthly.rename(columns={'Date': 'Month', 'Volume(V µg/m3)': 'Ozone Volume'}, inplace=True)

			# pm10Monthly = pm10Daily
			# pm10Monthly['Date'] = pd.to_datetime(pm10Monthly['Date'], infer_datetime_format=True)
			# pm10Monthly['Date'] = pm10Monthly['Date'].dt.to_period("M").dt.end_time.dt.strftime("%Y-%m")
			# pm10Monthly.rename(columns={'Date': 'Month', 'Volume(V µg/m3)': 'PM10 Volume'}, inplace=True)

			pm25Monthly = pm25Daily
			pm25Monthly['Date'] = pd.to_datetime(pm25Monthly['Date'], infer_datetime_format=True)
			pm25Monthly['Date'] = pm25Monthly['Date'].dt.to_period("M").dt.end_time.dt.strftime("%Y-%m")
			pm25Monthly.rename(columns={'Date': 'Month', 'Volume(V µg/m3)': 'PM2.5 Volume'}, inplace=True)

			nitroDioxideMonthly = nitroDioxideDaily
			nitroDioxideMonthly['Date'] = pd.to_datetime(nitroDioxideMonthly['Date'], infer_datetime_format=True)
			nitroDioxideMonthly['Date'] = nitroDioxideMonthly['Date'].dt.to_period("M").dt.end_time.dt.strftime("%Y-%m")
			nitroDioxideMonthly.rename(columns={'Date': 'Month', 'Volume(V µg/m3)': 'Nitrogen Dioxide Volume'}, inplace=True)

			#print(nitroDioxideMonthly)
			ozoneMonthly.drop_duplicates(subset='Month')
			pm25Monthly.drop_duplicates(subset='Month')
			nitroDioxideMonthly.drop_duplicates(subset='Month')
			multiData = [ozoneMonthly, pm25Monthly, nitroDioxideMonthly] # [ozoneMonthly, pm10Monthly, pm25Monthly, nitroDioxideMonthly]
			LECMonthly = reduce(lambda left, right: pd.merge(left, right, on='Month', how='left'), multiData)
			print(LECMonthly)
			
			graph.generateGraph("LEC", LECMonthly, timescale, mode)