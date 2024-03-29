import pandas as pd
import plotly.express as px
from sys import platform

# COLOURSCHEME = px.colors.sequential.algae

def loadCSV(dataset: str):
	if platform == "linux" or platform == "linux2":
		strFormat = rf"./example/csv/{dataset}.csv"
	elif platform == "win32":
		strFormat = rf".\csv\{dataset}.csv"
	csvLoaded = pd.read_csv(strFormat)
	return csvLoaded

def generateGraph(dataset: str, mode: str = "html", colour: str = "algae"):
    '''
    Generates a graph for given dataset

 	Parameters:
 		dataset: Choose the dataset to be plotted
  		mode: Choose the export mode you prefer
   		colour: Choose the colour scheme of the map (applies to globalVaccines only)
    '''
    print(f"Generating graph for '{dataset}' in mode '{mode}'")
    if dataset == "londonCases":
        csvLoaded = loadCSV(dataset)
        df = csvLoaded  # Loads data from csv and makes a dataframe in pandas
        fig = px.line(
            df,
            x='date',
            y='cumCasesBySpecimenDate',
            title='Daily New Cases in London',
            labels={
                "date": "Date",
                "cumCasesBySpecimenDate": "Total Cases"
            }
        )  # Creates a line graph using the 'date' and 'cumCasesBySpecimenDate' columns from the csv
    elif dataset == "usaCases":
        csvLoaded = loadCSV(dataset)
        df = csvLoaded
        fig = px.line(df,
                      x='date',
                      y='total_cases',
                      title='Daily New Cases in USA',
                      labels={
                          "date": "Date",
                          "total_cases": "Total Cases"
                      })
    elif dataset == "englandDeaths":
        csvLoaded = loadCSV(dataset)
        df = csvLoaded
        fig = px.line(df,
                      x='week',
                      y='deaths',
                      title='Weekly Covid Deaths in England',
                      labels={
                          "week": "Week Ending",
                          "deaths": "Weekly Deaths"
                      })
    elif dataset == "globalVaccines":
        csvLoaded = loadCSV(dataset)
        df = csvLoaded
        fig = px.choropleth(
            df,
            locations="ISO3",
            color="PERSONS_FULLY_VACCINATED_PER100",
            hover_name="COUNTRY",
            # hover_data={'VACCINES_USED', 'FIRST_VACCINE_DATE'},
			hover_data={'FIRST_VACCINE_DATE'},
            title="Global Vaccinations",
            color_continuous_scale=colour, #COLOURSCHEME,
            labels={
                "PERSONS_FULLY_VACCINATED_PER100":
                "% of Population Vaccinated",
                "ISO3": "Country Code",
                "FIRST_VACCINE_DATE": "Date of First Vaccination",
                #"VACCINES_USED": "List of Vaccine Types used",
            })
        # Creates a choropleth map of the vaccination data across the world based on the percentage of people fully vaccinated.
        # Also shows date of first vaccination and list of vaccine types used
        fig["layout"].pop("updatemenus")
    if mode == "web":
        fig.show(renderer="browser")  # Opens in the browser
    elif mode == "html":
        fig.write_html(f"{dataset}.html",
                       auto_open=True)  # Writes to static html file - Default
    elif mode == "html-connected":
        fig.write_html(
            f"{dataset}.html", include_plotlyjs="cdn", auto_open=True
        )  # Writes to html file with a much smaller file size, requires internet connection - Recommended
    elif mode == "png":
        fig.show(renderer="png"
                 )  # Creates png image - Requires kaleido library and ipython
    elif mode == "auto":
        fig.show()  # Let plotly automatically decide what renderer to use


generateGraph("globalVaccines", "html", "algae")
