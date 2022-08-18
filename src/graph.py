import plotly.express as px

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
            df = dataset
            fig = px.scatter(df,
                x='Week',
                y=['PM2.5 Volume', 'Volume(V µg/m3)'],
                title='Weekly Air Pollution',
                category_orders={"variable": ["PM2.5", "Nitrogen Dioxide"]},
                labels={
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
    if region == "LCC":
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
    fig.update_layout(legend_title_text='Pollutant')
    fig["layout"].pop("updatemenus")
    #print(fig)
    #fig.write_image(f"{region}-{time}.jpeg")
    if mode == "png":
        fig.write_image(f"{region}-{time}.png")
        print(f"Graph: Graph generated in '{region}-{time}.png'")
    elif mode == "html" or None:
        fig.write_html(f"{region}-{time}.html", auto_open=False, include_plotlyjs="cdn")
        print(f"Graph: Graph generated in '{region}-{time}.html'")