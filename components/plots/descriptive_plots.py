import plotly.express as px
import plotly.graph_objects as go
import requests
import folium
import plotly.io as pio
pio.templates

#ruta_datos = r"D:\\Documentos\\Certificación DS4A\\Proyecto\\Git final\\Por unir\\2\\DS4A_FINAL_PROJECT\\data"
ruta_datos = r"C:\\Users\\bolemm01\\OneDrive - CSG Systems Inc\\Desktop\\DS4A\\DS4A_COPY\\DS4A_FINAL_PROJECT\\data"




def get_scatter(df, eje_x, eje_y):
    fig = px.scatter(df, x=eje_x, y=eje_y)
    return fig


def get_map2(df):
    t = folium.Map([4.862437, -74.058655], zoom_start=11, tiles="Stamen Terrain")

    for index, row in df.iterrows():
        folium.CircleMarker([row['latitud'], row['longitud']],
                        radius=row['tallos_planta']*100,
                        popup=row['tallos_planta'],
                        tooltip=row['finca'],
                        fill_color="#3db7e4",
                       ).add_to(t)

    t.save(ruta_datos+'\\mymap.html')

def get_prod_edad(df):
    fig = px.line(df, x="edad", y="tallos_planta", color='finca', template='simple_white', labels={'edad':'Age(week)','tallos_planta':'Stems/plant', 'finca':'Farm'})
    return fig

def get_heatmap_temp_mean(df):  
    fig = go.Figure(data=go.Heatmap(
                   z=df.z,
                   x=df.x,
                   y=df.Hora_single,
                   xgap = 0.7,
                   ygap = 0.7,
                   colorscale='Viridis',
                   hoverongaps = False))

    fig.update_layout(
        yaxis = {'categoryorder':"total ascending"},
        xaxis = {'type':'category'},
    )

    return fig

def get_heatmap_temp_min(df):  
    fig = go.Figure(data=go.Heatmap(
                   z=df.z,
                   x=df.x,
                   y=df.Hora_single,
                   xgap = 0.7,
                   ygap = 0.7,
                   colorscale='Viridis',
                   hoverongaps = False))

    fig.update_layout(
        yaxis = {'categoryorder':"total ascending"},
        xaxis = {'type':'category'},
    )

    return fig

def get_heatmap_temp_max(df):  
    fig = go.Figure(data=go.Heatmap(
                   z=df.z,
                   x=df.x,
                   y=df.Hora_single,
                   xgap = 0.7,
                   ygap = 0.7,
                   colorscale='Viridis',
                   hoverongaps = False))

    fig.update_layout(
        yaxis = {'categoryorder':"total ascending"},
        xaxis = {'type':'category'},
    )

    return fig


def get_heatmap_rad_mean(df):  
    fig = go.Figure(data=go.Heatmap(
                   z=df.z,
                   x=df.x,
                   y=df.Hora_single,
                   xgap = 0.7,
                   ygap = 0.7,
                   colorscale='Viridis',
                   hoverongaps = False))

    fig.update_layout(
        yaxis = {'categoryorder':"total ascending"},
        xaxis = {'type':'category'},
    )

    return fig 