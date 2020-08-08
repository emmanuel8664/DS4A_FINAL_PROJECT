import plotly.express as px
import plotly.graph_objects as go
import requests
import folium
import plotly.io as pio
pio.templates
import datetime
datetime.datetime.strptime
import pandas as pd

def get_redes(df):
    fig = go.Figure()


    fig.update_layout(template="simple_white", title='Neural Network compliance vs Farm model compliance',
                   title_x=0.5,
                   xaxis_title='Date',
                   yaxis_title='Percentage of compliance',
                   yaxis= {
                    'tickformat':',.0%',
                    'range': [0,2]
                    })

    fig.add_trace(go.Scatter(x=df['dia'], y=df['%Cumplimiento_finca'],
                    mode='lines',
                    name='Farm Compliance'))

    fig.add_trace(go.Scatter(x=df['dia'], y=df['%Cumplimiento_red_neuronal'],
                    mode='lines',
                    name='Neural Network Compliance'))

    fig.add_trace(go.Scatter(x=df['dia'], y=df['lim_inf'],
                    mode='markers',
                    name='Low boundary 95%',
                    ))

    fig.add_trace(go.Scatter(x=df['dia'], y=df['lim_sup'],
                    mode='markers',
                    name='Upper boundary 115%',
                    ))

    return fig                                                                

def get_temp(df):
    fig = go.Figure()

    fig.update_layout(template="simple_white", title='Temperature prediction',
                   title_x=0.5,
                   xaxis_title='Date',
                   yaxis_title='Temperature change',)
    
    fig.add_trace(
    go.Scatter(x=list(df['list__dt_txt']),
               y=list(df['list__main__feels_like']),
               name="main/feels_like",
               line=dict(color="#11CFA5")))

    fig.add_trace(
    go.Scatter(x=list(df['list__dt_txt']),
               y=list(df['list__main__temp_min']),
               name="main/temp_min",
               line=dict(color="#33CFA7")))

    fig.add_trace(
    go.Scatter(x=list(df['list__dt_txt']),
               y=list(df['list__main__temp_max']),
               name="main/temp_max",
               line=dict(color="#F06A6A")))                      

    return fig

def get_temp2(df):
    fig = go.Figure(data=[go.Candlestick(
        x=df['list__dt_txt'], 
        open=df['list__main__temp_min'],high=df['list__main__temp_min'],
        low=df['list__main__temp_max'], close=df['list__main__temp_max'],
        increasing_line_color= 'cyan', decreasing_line_color= 'gray')])

    fig.update_layout(template="simple_white", title='Min vs Max vs Mean feels like',
                   title_x=0.5,
                   xaxis_title='Date',
                   yaxis_title='Temperature change',)

    return fig
    
def get_wind(df2):
    df = px.data.wind()
    fig = px.bar_polar(df2, r="count", theta="direction", color="range", template="simple_white",
            color_discrete_sequence= px.colors.sequential.Plasma_r) 

    return fig        

def get_proyeccion(df,max_date):
    

    fig = go.Figure()
    fig.update_layout(template="simple_white", title='Neural Network Forecast',
                   title_x=0.5,
                   xaxis_title='Date',
                   yaxis_title='Total Stems')

    max=max_date
    try:
        pron = df[df['dia']>=max]
        real = df[df['dia']<max]
    except:
        pron = df[df['dia']>=datetime.date(2020,3,21)]
        real = df[df['dia']<datetime.date(2020,3,21)]


    fig.add_trace(go.Scatter(x=real['dia'], y=real['tallos_metodo_finca'],
            mode='lines+markers',
            name='Farm'))        

    fig.add_trace(go.Scatter(x=real['dia'], y=real['tallos_red'],
            mode='lines+markers',
            name='Neural Network',
            marker_color='rgba(255,127,14,1)'))

    fig.add_trace(go.Scatter(x=pron['dia'], y=pron['tallos_red'],
                    mode='markers',
                    name='Neural Network Forecast',
                    marker_color='rgba(255,127,14,1)'))

    return fig     