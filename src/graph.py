import plotly.express as px
import pprint

regionNames = {
        "LWM": "London Westminster",
        "NCC": "Newcastle Centre",
        "LEC": "Leeds Centre"
    }

def generateGraph(region, dataset, time, mode=None):
    '''
    Generates a graph for regional data and writes to an HTML file

 	Parameters:
 		region: Choose the region to be plotted
  		data: Uses the dataset from the pipeline
   		time: Weekly or Monthly (Daily?)
    '''
    print(f"Graph: Generating graph for '{region}'")
    if region == "LWM":
        if time == "WEEKLY":
            df = dataset # Loads dataset that has gone through pipeline.py
            fig = px.scatter(df, # Creates a scatter plot in Plotly using the data from the pipeline
                x='Week', # Using the column name that has been given by the pipeline
                y=['PM2.5 Volume', 'Volume(V µg/m3)'], # Using the column names from the CSV files
                title='Weekly Air Pollution', # Initial graph title, region name to be added after
                category_orders={"variable": ["PM2.5", "Nitrogen Dioxide"]}, # Correctly order the pollutants
                labels={ # Update labels on graph for user readability
                    "variable": "Pollutant",
                    "value": "Volume (V µg/m3)",
                }
            )
        if time == "MONTHLY":
            df = dataset
            fig = px.scatter(df,
                x='Month',
                y=['PM2.5 Volume', 'Volume(V µg/m3)'],
                title='Monthly Air Pollution',
                category_orders={"variable": ["PM2.5", "Nitrogen Dioxide"]},
                labels={
                    "variable": "Pollutant",
                    "value": "Volume (V µg/m3)",
                }
            )
        newLabels = {'PM2.5 Volume':'PM2.5', 'Volume(V µg/m3)': 'Nitrogen Dioxide'}
        fig.for_each_trace(lambda t: t.update(name = newLabels[t.name],
                                      legendgroup = newLabels[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newLabels[t.name])
                                     )
                  )
    if region == "NCC":
        if time == "WEEKLY":
            df = dataset
            fig = px.scatter(df,
                x='Week',
                y=['Ozone Volume', 'PM2.5 Volume', 'Nitrogen Dioxide Volume'], # ['Ozone Volume', 'PM10 Volume', 'PM2.5 Volume', 'Nitrogen Dioxide Volume'],
                title='Weekly Air Pollution',
                labels={
                    "variable": "Pollutant",
                    "value": "Volume (V µg/m3)",
                }
            )
        if time == "MONTHLY":
            df = dataset
            fig = px.scatter(df,
                x='Month',
                y=['Ozone Volume', 'PM2.5 Volume', 'Nitrogen Dioxide Volume'], # ['Ozone Volume', 'PM10 Volume', 'PM2.5 Volume', 'Nitrogen Dioxide Volume'],
                title='Monthly Air Pollution',
                labels={
                    "variable": "Pollutant",
                    "value": "Volume (V µg/m3)",
                }
            )
        newLabels = {'Ozone Volume':'Ozone', 'PM2.5 Volume': 'PM2.5', 'Nitrogen Dioxide Volume': 'Nitrogen Dioxide'}
        fig.for_each_trace(lambda t: t.update(name = newLabels[t.name],
                                      legendgroup = newLabels[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newLabels[t.name])
                                     )
                  )
    if region == "LEC":
        if time == "WEEKLY":
            df = dataset
            fig = px.scatter(df,
                x='Week',
                y=['Ozone Volume', 'PM2.5 Volume', 'Nitrogen Dioxide Volume'], # ['Ozone Volume', 'PM10 Volume', 'PM2.5 Volume', 'Nitrogen Dioxide Volume'],
                title='Weekly Air Pollution',
                labels={
                    "variable": "Pollutant",
                    "value": "Volume (V µg/m3)",
                }
            )
        if time == "MONTHLY":
            df = dataset
            fig = px.scatter(df,
                x='Month',
                y=['Ozone Volume', 'PM2.5 Volume', 'Nitrogen Dioxide Volume'], # ['Ozone Volume', 'PM10 Volume', 'PM2.5 Volume', 'Nitrogen Dioxide Volume'],
                title='Monthly Air Pollution',
                labels={
                    "variable": "Pollutant",
                    "value": "Volume (V µg/m3)",
                }
            )
        newLabels = {'Ozone Volume':'Ozone', 'PM2.5 Volume': 'PM2.5', 'Nitrogen Dioxide Volume': 'Nitrogen Dioxide'}
        fig.for_each_trace(lambda t: t.update(name = newLabels[t.name],
                                      legendgroup = newLabels[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newLabels[t.name])
                                     )
                  )
    fig.update_layout(legend_title_text='Pollutant', title=f"{fig.layout.title.text} - {regionNames[region]}")
    fig["layout"].pop("updatemenus")
    #print(fig)
    #fig.write_image(f"{region}-{time}.jpeg")
    if mode == "PNG":
        fig.write_image(f"{region}-{time}.png")
        print(f"Graph: Graph generated in '{region}-{time}.png'")
    elif mode == "HTML-OFFLINE":
        fig.write_html(f"{region}-{time}.html", auto_open=False)
        print(f"Graph: Graph generated in '{region}-{time}.html'")
    elif mode == "HTML" or None:
        fig.write_html(f"{region}-{time}.html", auto_open=False, include_plotlyjs="cdn")
        print(f"Graph: Graph generated in '{region}-{time}.html'")