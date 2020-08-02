import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from components.filters import Filter
from components.data_controllers.descriptive_data import descriptive_data
from components.plots import descriptive_plots


descriptive_data = descriptive_data()
filtro = Filter()
#ruta_datos = r"D:\\Documentos\\Certificación DS4A\\Proyecto\\Git final\\Por unir\\2\\DS4A_FINAL_PROJECT\\data"
ruta_datos = r"C:\\Users\\bolemm01\\OneDrive - CSG Systems Inc\\Desktop\\DS4A\\DS4A_COPY\\DS4A_FINAL_PROJECT\\data"

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
                    ]
                ),
            ]
        )
    )

def build_content():
    figuras = get_figuras()
    return [
        html.Div
        (
            id="map_first_graph",
            children=
            [
                html.B("Coefficients"),
                html.Hr(),
                html.Iframe(id='mapFincas',srcDoc = open(ruta_datos+'\\mymap.html', 'r').read(),width='100%',height='600')
            ],
        ),
        
        html.Div
        (
            id="wait_time_card",
            children=
            [
                html.B("Production by age"),
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
    return  dbc.Tabs(
            [
                dbc.Tab(build_heatmap_temp_mean(), label="AVG Temperature"),
                dbc.Tab(build_heatmap_temp_max(), label="MAX Temperature"),
                dbc.Tab(build_heatmap_temp_min(), label="MIN Temperature"),
                dbc.Tab(build_heatmap_rad_mean(), label="AVG Radiation")
            ],
            id="tabs2",
            active_tab="descriptive2",
            className="navbar navbar-expand-md",
        )

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
    get_map2()
    figuras['prod_edad'] = get_prod_edad()
    figuras['heatmap_temp_mean'] = get_heatmap_temp_mean()
    figuras['heatmap_temp_min']= get_heatmap_temp_min()
    figuras['heatmap_temp_max']= get_heatmap_temp_max()
    figuras['heatmap_rad_mean']= get_heatmap_rad_mean()
    return figuras


def get_map2():
    df = descriptive_data.get_map2()
    descriptive_plots.get_map2(df)



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