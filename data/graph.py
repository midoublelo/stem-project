import pandas as pd
import plotly.express as px

### USA Cases
df = pd.read_csv(r"C:\Users\Millo\Desktop\Spirefall\Projects\stem-project\usaCases.csv")
fig = px.line(df, x = 'date', y = 'total_cases', title='Daily New Cases in USA')

### London Cases
# df = pd.read_csv(r"C:\Users\Millo\Desktop\Spirefall\Projects\stem-project\londonCases.csv")
# fig = px.line(df, x = 'date', y = 'cumCasesBySpecimenDate', title='Daily New Cases in London')

### England Deaths
# df = pd.read_csv(r"C:\Users\Millo\Desktop\Spirefall\Projects\stem-project\englandDeaths.csv")
# fig = px.line(df, x = 'week', y = 'deaths', title='Weekly Covid Deaths in England')

### Global Vaccinations
# df = pd.read_csv(r"C:\Users\Millo\Desktop\Spirefall\Projects\stem-project\globalVaccines.csv")
# fig = px.choropleth(df, locations="ISO3",
#                     color="PERSONS_FULLY_VACCINATED_PER100",
#                     hover_name="COUNTRY",
#                     hover_data={'VACCINES_USED', 'FIRST_VACCINE_DATE'},
#                     # animation_frame="DATE_UPDATED",
#                     title = "Global Vaccinations",
# )
# fig["layout"].pop("updatemenus")
fig.write_html('test.html', auto_open=True)
# fig.show()