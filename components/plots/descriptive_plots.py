import plotly.express as px
import plotly.graph_objects as go
import requests
import folium


def get_hist(df, eje_x, eje_y):
    #data_canada = data[data.country == 'Canada']
    fig = px.histogram(df, x=eje_x, y=eje_y,
             hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
             labels={'pop':'population of Canada'}, height=400)
    return fig

def get_boxplot(df, eje_x, eje_y):
    fig = px.box(df, x=eje_x, y=eje_y, color="smoker")
    fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
    return fig

def get_heatmap():
    fig = go.Figure(data=go.Heatmap(
                   z=[[1, None, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                   x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                   y=['Morning', 'Afternoon', 'Evening']))#,
                   #hoverongaps = False))
    return fig

def get_line():
    # Add data
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
    high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
    low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
    high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
    low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
    high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
    low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]
    
    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=month, y=high_2014, name='High 2014',
    line=dict(color='firebrick', width=4)))
    fig.add_trace(go.Scatter(x=month, y=low_2014, name = 'Low 2014',
    line=dict(color='royalblue', width=4)))
    fig.add_trace(go.Scatter(x=month, y=high_2007, name='High 2007',
    line=dict(color='firebrick', width=4,dash='dash') # dash options include 'dash', 'dot', and 'dashdot'
    ))
    fig.add_trace(go.Scatter(x=month, y=low_2007, name='Low 2007',
    line = dict(color='royalblue', width=4, dash='dash')))
    fig.add_trace(go.Scatter(x=month, y=high_2000, name='High 2000',
    line = dict(color='firebrick', width=4, dash='dot')))
    fig.add_trace(go.Scatter(x=month, y=low_2000, name='Low 2000',
    line=dict(color='royalblue', width=4, dash='dot')))
    # Edit the layout
    fig.update_layout(title='Average High and Low Temperatures in New York',
    xaxis_title='Month',yaxis_title='Temperature (degrees F)')
    return fig

#def get_map(df, eje_x, eje_y):
def get_map(df):
    repo_url = 'https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json' #Archivo GeoJSON
    mx_regions_geo = requests.get(repo_url).json()

    limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]
    colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
    cities = []
    scale = 5000
    fig = go.Figure()
    for i in range(len(limits)):
        lim = limits[i]
        df_sub = df[lim[0]:lim[1]]
        fig.add_trace(go.Scattergeo(
            locations = ["Colombia"],
            locationmode = 'country names',
            #locationmode = 'USA-states',
            lon = df_sub['lon'],
            lat = df_sub['lat'],
            text = df_sub['text'],
            marker = dict(
                size = df_sub['pop']/scale,color = colors[i],
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode = 'area'
            ),
            name = '{0} - {1}'.format(lim[0],lim[1])))
    fig.update_layout(
        title_text = '2014 US city populations<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope = 'south america',
            landcolor = 'rgb(217, 217, 217)',
        )
    )
    return fig

def get_scatter(df, eje_x, eje_y):
    fig = px.scatter(df, x=eje_x, y=eje_y)
    return fig


def get_map2(df):
    t = folium.Map([4.862437, -74.058655], zoom_start=11, tiles="Stamen Toner")

    for index, row in df.iterrows():
        folium.CircleMarker([row['latitud'], row['longitud']],
                        radius=row['tallos_planta']*100,
                        popup=row['tallos_planta'],
                        tooltip=row['finca'],
                        fill_color="#3db7e4",
                       ).add_to(t)

    t.save('C:\\Users\\bolemm01\\Desktop\\Correlation1\\PROYECTO_FINAL\\assets\\mymap.html')
