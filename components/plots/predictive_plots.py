import plotly.express as px
import plotly.graph_objects as go
import requests
import folium
import plotly.io as pio
pio.templates


def get_redes(df):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df['dia'], y=df['%Cumplimiento_finca'],
                    mode='lines',
                    name='Cumplimiento finca'))

    fig.add_trace(go.Scatter(x=df['dia'], y=df['%Cumplimiento_red_neuronal'],
                    mode='lines',
                    name='Cumplimiento red neuronal'))

    fig.add_trace(go.Scatter(x=df['dia'], y=df['lim_inf'],
                    mode='markers',
                    name='Limite inferior 95%'))

    fig.add_trace(go.Scatter(x=df['dia'], y=df['lim_sup'],
                    mode='markers',
                    name='Limite superior 115%'))
    return fig                                                                

def get_temp(df):
    fig = go.Figure()
    
    fig.add_trace(
    go.Scatter(x=list(df['dt_txt']),
               y=list(df['main/feels_like']),
               name="main/feels_like",
               line=dict(color="#11CFA5")))

    fig.add_trace(
    go.Scatter(x=list(df['dt_txt']),
               y=list(df['main/temp_min']),
               name="main/temp_min",
               line=dict(color="#33CFA7")))

    fig.add_trace(
    go.Scatter(x=list(df['dt_txt']),
               y=list(df['main/temp_max']),
               name="main/temp_max",
               line=dict(color="#F06A6A")))                      

    return fig

def get_temp2(df):
     fig = go.Figure(data=[go.Candlestick(
     x=df['dt_txt'],
     open=df['main/temp_min'],high=df['main/temp_min'],
     low=df['main/temp_max'], close=df['main/temp_max'],
     increasing_line_color= 'cyan', decreasing_line_color= 'gray')])

     return fig