import pandas as pd
import plotly.express as px

def generateGraph(dataset: str, mode: str):
    '''
    Generates a graph for given dataset
    '''
    if dataset == "londonCases":
        df = pd.read_csv(r"C:\Users\Millo\Desktop\Spirefall\Projects\stem-project\londonCases.csv") # Loads data from csv and makes a dataframe in pandas
        fig = px.line(df, x = 'date', y = 'cumCasesBySpecimenDate', title='Daily New Cases in London') # Creates a line graph using the 'date' and 'cumCasesBySpecimenDate' columns from the csv
    elif dataset == "usaCases":
        df = pd.read_csv(r"C:\Users\Millo\Desktop\Spirefall\Projects\stem-project\usaCases.csv")
        fig = px.line(df, x = 'date', y = 'total_cases', title='Daily New Cases in USA')
    elif dataset == "englandDeaths":
        df = pd.read_csv(r"C:\Users\Millo\Desktop\Spirefall\Projects\stem-project\englandDeaths.csv")
        fig = px.line(df, x = 'week', y = 'deaths', title='Weekly Covid Deaths in England')
    elif dataset == "globalVaccines":
        df = pd.read_csv(r"C:\Users\Millo\Desktop\Spirefall\Projects\stem-project\globalVaccines.csv")
        fig = px.choropleth(df, locations="ISO3",
                            color="PERSONS_FULLY_VACCINATED_PER100",
                            hover_name="COUNTRY",
                            hover_data={'VACCINES_USED', 'FIRST_VACCINE_DATE'},
                            title = "Global Vaccinations",
        ) # Creates a choropleth map of the vaccination data across the world based on the percentage of people fully vaccinated. Also shows date of first vaccination and list of vaccine types used
        fig["layout"].pop("updatemenus")
    if mode == "web":
        fig.show(renderer="browser") # Opens in the browser
    elif mode == "html":
        fig.write_html('graph.html', auto_open=True) # Writes to static html file - Recommended
    elif mode == "html-connected":
        fig.write_html('graph.html', include_plotlyjs="cdn", auto_open=True) # Writes to html file with a much smaller file size, requires internet connection
    elif mode == "png":
        fig.show(renderer="png") # Creates png image

generateGraph("globalVaccines", "html-connected")
