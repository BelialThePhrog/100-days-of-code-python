import chart_studio.plotly as py
import plotly.graph_objs as go
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# Initialize offline notebook environment
init_notebook_mode(connected=True)

# ==========================================
# 1. SIMPLE US STATE PROTOTYPE
# ==========================================
data_simple = dict(
    type='choropleth',
    locations=['AZ', 'CA', 'NY'],
    locationmode='USA-states',
    colorscale='Greens',
    text=['text1', 'text2', 'text3'],
    z=[1.0, 2.0, 3.0],
    colorbar={'title': 'Colorbar Title'}
)

layout_simple = dict(geo={'scope': 'usa'})

choromap_simple = go.Figure(data=[data_simple], layout=layout_simple)
# Use plot() for standalone Python execution, iplot() for interactive notebooks
plot(choromap_simple, filename='simple_us_choropleth.html')


# ==========================================
# 2. REAL US AGRICULTURAL EXPORTS (2011)
# ==========================================
df_agri = pd.read_csv('2011_US_AGRI_Exports')

data_agri = dict(
    type='choropleth',
    colorscale='portland',
    locations=df_agri['code'],
    z=df_agri['total exports'],
    locationmode='USA-states',
    text=df_agri['text'],
    marker=dict(line=dict(color='rgb(255,255,255)', width=2)),
    colorbar={'title': "Millions USD"}
)

layout_agri = dict(
    title='2011 US Agriculture Exports by State',
    geo=dict(
        scope='usa',
        showlakes=True,
        lakecolor='rgb(85,173,240)'
    )
)

choromap_agri = go.Figure(data=[data_agri], layout=layout_agri)
plot(choromap_agri, filename='us_agri_exports_2011.html')


# ==========================================
# 3. GLOBAL GDP CHOROPLETH MAP (2014)
# ==========================================
df_gdp = pd.read_csv('2014_World_GDP')

data_gdp = dict(
    type='choropleth',
    locations=df_gdp['CODE'],
    z=df_gdp['GDP (BILLIONS)'],
    text=df_gdp['COUNTRY'],
    colorbar={'title': 'GDP Billions US'}
)

layout_gdp = dict(
    title='2014 Global GDP',
    geo=dict(
        showframe=False,
        projection={'type': 'bonne'}
    )
)

choromap_gdp = go.Figure(data=[data_gdp], layout=layout_gdp)
plot(choromap_gdp, filename='world_gdp_2014.html')
