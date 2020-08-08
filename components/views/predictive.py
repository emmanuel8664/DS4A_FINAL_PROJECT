import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from components.predictive_filters import Predictive_filter
from components.data_controllers.predictive_data import predictive_data
from components.plots import predictive_plots

predictive_data = predictive_data()
filtro = Predictive_filter()


def build_predictive():
    return dbc.Card(
        html.Div
        (
            [
                dbc.Row
                (
                    [
                        dbc.Col
                        (
                            [
                                html.Div
                                (
                                    filtro.get_filtro()
                                ),

                                html.Div("Wind force and direction"),
                                html.Div
                                (   
                                    dcc.Graph(id = 'wind', figure = get_wind())
                                )
                            ],
                            md=3
                        ),
                        dbc.Col
                        (
                            html.Div
                            (
                                id="right-column2",
                                className="eight columns",
                                children=build_content()
                            ),
                        )
                    ]
                ),
            ]
        )
    )

def build_tabs3():
    return  dbc.Tabs(
            [
                dbc.Tab(build_graph_temp_2(), label="Temperature Change"),
                dbc.Tab(build_graph_temp_1(), label="Meanfeals vs Temperature"),
            ],
            id="tabs3",
            className="navbar navbar-expand-md",
        )


def build_tabs4():
    return  dbc.Tabs(
            [
                dbc.Tab(build_graph_red_2(), label="Forecast"),
                dbc.Tab(build_graph_red_1(), label="Compliance"),
                
            ],
            id="tabs4",
            className="navbar navbar-expand-md",
        )

def build_graph_red_1():
    figuras = get_figuras()
    return dbc.Card(html.Div(dcc.Graph(id = 'red1', figure=figuras['red_neuronal'])))

def build_graph_red_2():
    figuras = get_figuras()
    return dbc.Card(html.Div(dcc.Graph(id = 'red2', figure=figuras['proyeccion'])))

def build_graph_temp_1():
    figuras = get_figuras()
    return dbc.Card(html.Div(dcc.Graph(id = 'temperatura1', figure=figuras['temp'])))

def build_graph_temp_2():
    figuras = get_figuras()
    return dbc.Card(html.Div(dcc.Graph(id = 'temperatura2', figure=figuras['temp2'])))

def build_content():
    figuras = get_figuras()
    return [
        html.Div
        (
            id="proyeccion",
            children=build_tabs4()
        ),
        html.Div
        (
            id="temperatura",
            children=build_tabs3()
                
        )
    ]

def get_figuras():
    figuras = {}
    figuras['red_neuronal'] = get_redes()
    figuras['temp'] = get_temp()
    figuras['temp2'] = get_temp2()
    figuras['wind'] = get_wind()
    figuras['proyeccion'] = get_pronostico()
    return figuras   

def get_redes():
    df2 = predictive_data.get_redes()
    red = predictive_plots.get_redes(df2)
    return red
    

def get_temp():
    df3 = predictive_data.get_temp()
    temp = predictive_plots.get_temp(df3)
    return temp

def get_temp2():
    df4 = predictive_data.get_temp()
    temp2 = predictive_plots.get_temp2(df4)
    return temp2


def get_wind():
    df5 = predictive_data.get_wind()
    wind = predictive_plots.get_wind(df5)
    return wind

def get_pronostico():
    df6 = predictive_data.get_proyeccion()
    max_data = predictive_data.get_max_data()
    proy = predictive_plots.get_proyeccion(df6,max_data)
    return proy
