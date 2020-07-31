import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from components.filters import Filter
from components.data_controllers.predictive_data import predictive_data
from components.plots import predictive_plots

predictive_data = predictive_data()


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
                            html.Div
                            (
                                #filtro.get_filtro()
                            ),
                            md=2
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
                        # dbc.Col(html.Div([
                        # dcc.Graph(figure=fig)
                        # ]),md=8)
                        #dbc.Col(dbc.Row([dbc.Col(html.Div("Content1"),md=6),dbc.Col(html.Div("Content2"),md=6)]),md=8),
                    ]
                ),
            ]
        )
    )



def build_content():
    figuras = get_figuras()
    return [
        # Patient Volume Heatmap
        html.Div
        (
            id="proyeccion",
            children=
            [
                html.B("Proyeccion"),
                dcc.Graph(figure = figuras['red_neuronal']),
            ],
        ),
        # Patient Wait time by Department
        html.Div
        (
            id="temperatura",
            children=
            [
                html.B("Temperatura"),
                dcc.Graph(figure = figuras['temp2']),
                
            ],
        )
    ]

def get_figuras():
    figuras = {}
    figuras['red_neuronal'] = get_redes()
    figuras['temp'] = get_temp()
    figuras['temp2'] = get_temp2()
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