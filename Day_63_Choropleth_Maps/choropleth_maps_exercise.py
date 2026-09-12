import chart_studio.plotly as py
import plotly.graph_objs as go
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# Initialize offline notebook environment
init_notebook_mode(connected=True)

# ==========================================
# EXERCISE 1: WORLD POWER CONSUMPTION (2014)
# ==========================================
df_power = pd.read_csv('2014_World_Power_Consumption')

data_power = dict(
    type='choropleth',
    locations=df_power['Country'],
    locationmode='country names',
    z=df_power['Power Consumption KWH'],
    text=df_power['Text'],
    colorbar={'title': 'Power_com'}
)

layout_power = dict(
    title='2014 Power',
    geo=dict(
        showframe=False,
        projection={'type': 'bonne'}
    )
)

choromap_power = go.Figure(data=[data_power], layout=layout_power)
plot(choromap_power, filename='world_power_consumption_2014.html')


# ==========================================
# EXERCISE 2: USA VOTING-AGE POPULATION (2012)
# ==========================================
df_election = pd.read_csv('2012_Election_Data')

data_election = dict(
    type='choropleth',
    colorscale='portland',
    locations=df_election['State Abv'],
    z=df_election['Voting-Age Population (VAP)'],
    locationmode='USA-states',
    text=df_election['State'],
    marker=dict(line=dict(color='rgb(255,255,255)', width=2)),
    colorbar={'title': "Voting-Age Population"}
)

layout_election = dict(
    title='2012 Voting-Age Population',
    geo=dict(
        scope='usa',
        showlakes=True,
        lakecolor='rgb(85,173,240)'
    )
)

choromap_election = go.Figure(data=[data_election], layout=layout_election)
plot(choromap_election, filename='us_voting_age_population_2012.html')
