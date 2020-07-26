import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from components.filters import Filter
from components.data_controllers.descriptive_data import descriptive_data
from components.plots import descriptive_plots


descriptive_data = descriptive_data()
filtro = Filter()

def build_descriptive():
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
                                filtro.get_filtro()
                            ),
                            md=4
                        ),
                        dbc.Col
                        (
                            html.Div
                            (
                                id="right-column",
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
            id="map_first_graph",
            children=
            [
                html.B("Fincas con su coeficiente"),
                html.Hr(),
                html.Iframe(id='mapFincas',srcDoc = open('C:\\Users\\bolemm01\\Desktop\\Correlation1\\PROYECTO_FINAL\\assets\\mymap.html', 'r').read(),width='100%',height='600')
                #dcc.Graph(figure = figuras['map']),
            ],
        ),
        # Patient Wait time by Department
        html.Div
        (
            id="wait_time_card",
            children=
            [
                html.B("Patient Wait Time and Satisfactory Scores"),
                html.Hr(),
                dcc.Graph(figure=figuras['heat_map']),
            ],
        ),
        html.Div
        (
            id="wait_time_card2",
            children=
            [
                html.B("Patient Wait Time and Satisfactory Scores"),
                html.Hr(),
                dcc.Graph(figure=figuras['line']),
            ],
        ),
    ]

def get_figuras():
    figuras = {}
    figuras['map'] = get_map2()
    figuras['heat_map'] = get_heatmap()
    figuras['line'] = get_line()
    return figuras

def get_map():
    df = descriptive_data.get_map()
    #mapa = descriptive_plots.get_map(df, descriptive_data.get_eje_x(), descriptive_data.get_eje_y())
    mapa = descriptive_plots.get_map(df)
    return mapa


 
def get_heatmap():
    #df = descriptive_data.get_heatmap()
    #mapa = descriptive_plots.get_map(df, descriptive_data.get_eje_x(), descriptive_data.get_eje_y())
    heat_mapa = descriptive_plots.get_heatmap()
    return heat_mapa

def get_line():
    line = descriptive_plots.get_line()
    return line

# def build_descriptive():
#     return [
#         html.H6("Descriptive"),
#         html.Br(),
#         html.P("Here you can see a behaviour over time of the icfes results and different socioeconomic factors in all Colombia")
#     ]

def get_map2():
    df = descriptive_data.get_map2()
    #mapa = descriptive_plots.get_map(df, descriptive_data.get_eje_x(), descriptive_data.get_eje_y())
    mapa2 = descriptive_plots.get_map2(df)
    return mapa2 