import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from components.filters import Filter
from components.data_controllers.descriptive_data import descriptive_data
from components.plots import descriptive_plots


descriptive_data = descriptive_data()
filtro = Filter()
ruta_datos = r"D:\\Documentos\\Certificación DS4A\\Proyecto\\Git final\\DS4A_FINAL_PROJECT\\data"
#ruta_datos = r"C:\\Users\\bolemm01\\Desktop\\Correlation1\\PROYECTO_FINAL\\data"

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
                html.Iframe(id='mapFincas',srcDoc = open(ruta_datos+'\\mymap.html', 'r').read(),width='100%',height='600')
                #dcc.Graph(figure = figuras['map']),
            ],
        ),
        # Patient Wait time by Department
        html.Div
        (
            id="wait_time_card",
            children=
            [
                html.B("Gráficos"),
                html.Hr(),
                dcc.Graph(id='fig_desc_prod_edad', figure=figuras['prod_edad']),
                
            ],
        ),
        html.Div
        (
            id="wait_time_card2",
            children=build_tabs2()
            
        ),
    ]

def build_tabs2():
    
    print('Construcción de los mapas de calor')
    return  dbc.Tabs(
            [
                dbc.Tab(build_heatmap_temp_mean(), label="Temperatura_promedio"),
                dbc.Tab(build_heatmap_temp_max(), label="Temperatura_máxima"),
                dbc.Tab(build_heatmap_temp_min(), label="Temperatura_mínima"),
                dbc.Tab(build_heatmap_rad_mean(), label="Radiación_promedio")
            ],
            id="tabs2",
            active_tab="descriptive2",
            className="navbar navbar-expand-md",
        )

#   return dbc.Card(html.Div(dcc.Graph(figure=figuras['bar'])))

def build_heatmap_temp_mean():
    figuras = get_figuras()
    return dbc.Card(html.Div(dcc.Graph(id = 'heatmap_temp_mean', figure=figuras['heatmap_temp_mean'])))

def build_heatmap_temp_max():
    figuras = get_figuras()
    return dbc.Card(html.Div(dcc.Graph(id = 'heatmap_temp_max', figure=figuras['heatmap_temp_max'])))

def build_heatmap_temp_min():
    figuras = get_figuras()
    return dbc.Card(html.Div(dcc.Graph(id = 'heatmap_temp_min', figure=figuras['heatmap_temp_min'])))

def build_heatmap_rad_mean():
    figuras = get_figuras()
    return dbc.Card(html.Div(dcc.Graph(id = 'heatmap_rad_mean', figure=figuras['heatmap_rad_mean'])))       


def get_figuras():
    figuras = {}
    #figuras['map'] = get_map2()
    get_map2()
    figuras['heat_map'] = get_heatmap()
    figuras['line'] = get_line()
    figuras['prod_edad'] = get_prod_edad()
    figuras['heatmap_temp_mean'] = get_heatmap_temp_mean()
    figuras['heatmap_temp_min']= get_heatmap_temp_min()
    figuras['heatmap_temp_max']= get_heatmap_temp_max()
    figuras['heatmap_rad_mean']= get_heatmap_rad_mean()
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
    #mapa2 = descriptive_plots.get_map2(df)
    descriptive_plots.get_map2(df)
    #return mapa2


def get_prod_edad():
    df2 = descriptive_data.get_prod_edad()
    prod_edad = descriptive_plots.get_prod_edad(df2)
    return prod_edad

def get_heatmap_temp_mean():
    df3 = descriptive_data.get_heatmap_temp_mean()
    heatMap_temp_med = descriptive_plots.get_heatmap_temp_mean(df3)
    return heatMap_temp_med

def get_heatmap_temp_min():
    df3 = descriptive_data.get_heatmap_temp_min()
    heatMap_temp_min = descriptive_plots.get_heatmap_temp_min(df3)
    return heatMap_temp_min

def get_heatmap_temp_max():
    df4 = descriptive_data.get_heatmap_temp_max()
    heatMap_temp_max = descriptive_plots.get_heatmap_temp_max(df4)
    return heatMap_temp_max

def get_heatmap_rad_mean():
    df5 = descriptive_data.get_heatmap_rad_mean()
    heatMap_rad_mean = descriptive_plots.get_heatmap_rad_mean(df5)
    return heatMap_rad_mean