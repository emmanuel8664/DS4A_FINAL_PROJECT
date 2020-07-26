import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd

from components.data_access.file_access import file_access

class Filter:
    class __filter:
        filtros = []
        def __init__(self):
            pass
        def __str__(self):
            return repr(self)
        def get_num_filtros(self):
            return len(self.filtros)
        def get_filtro(self):
            self.inicializar_filtro()
            return self.filtros[-1]
        def inicializar_filtro(self):
            id = self.get_num_filtros()
            data_access = file_access()
            data_produccion = data_access.get_df_produccion()
            list_variedades = data_produccion['variedad'].unique()
            list_fincas = data_produccion['finca'].unique()
            list_colors = data_produccion['Color'].unique()
            list_colors = list_colors
            list_colors_without_nan=np.delete(list_colors,22)
            
            list_dates = np.sort(data_produccion['anosemana'].unique())
            list_dates_converted = pd.to_datetime(list_dates)
            initial_value = list_dates_converted[0]
            last_value = list_dates_converted[len(list_dates_converted)-1]

            type_flowers = ["All ", "Claveles", "Miniclaveles"]
            filtro = dbc.Card(
                [
                    dbc.FormGroup(
                        [
                            html.P("Filtro por semana de la planta",className="control_label"),
                            dcc.DatePickerRange(
                            id="date_filter",
                            start_date_placeholder_text="Fecha Inicio",
                            end_date_placeholder_text="Fecha Fin",
                            #clearable=True,
                            #with_portal=True,
                            calendar_orientation='vertical',)  
                        ]
                    ),
                     dbc.FormGroup(
                        [
                            html.P("Filtro para fincas:", className="control_label"),
                            dbc.RadioItems(id="radio-fincas"+str(id),options=[{"label": "All", "value": 1},],),                
                            dcc.Dropdown(id="categoria"+str(id),options=[{"label": col, "value": col} for col in list_fincas],multi=True,value=list_fincas,className="dcc_control",),
                           
                        ]
                    ),
                     dbc.FormGroup(
                        [
                            html.P("Filtro para colores:", className="control_label"),
                            dbc.RadioItems(id="radio-color"+str(id),options=[{"label": "All", "value": 1},],),                
                            dcc.Dropdown(id="categoria-color"+str(id),options=[{"label": col, "value": col} for col in list_colors_without_nan],multi=True,value=list_colors_without_nan,className="dcc_control",),
                           
                        ]
                    ),
                    dbc.FormGroup(
                        [
                            dbc.Label(u"Variedades"),
                            dbc.RadioItems(
                                id="radio-variedades"+str(id),
                                options=[
                                    {"label": "All", "value": 1},
                                    {"label": "Claveles", "value": 2},
                                    {"label": "Mini Claveles", "value": 3},
                                ],
                            ),
                            dcc.Dropdown(
                                id="nivelCritica"+str(id),
                                options=[
                                    {"label": col, "value": col}  for col in list_variedades
                                ],
                                multi=True,
                                value=list_variedades,
                                className="dcc_control",
                            ),
                        ]
                    )
                ],
                body=True,
            )
            self.filtros.append(filtro)
    instance = None
    def __init__(self):
        if not Filter.instance:
            Filter.instance = Filter.__filter()
    def get_filtro(self):
        return self.instance.get_filtro()
    #def __getattribute__(self, name):
        #return getattr(self.instance, name)


#from components.data_load import *


'''def get_filtros():
    return dbc.Card
    (
        [
            dbc.FormGroup
            (
                [
                    html.P
                    (
                        "Filtro por semana de la planta", className="control_label",
                    ), dcc.RangeSlider
                    (
                        id="year_slider", min=1960, max=2017, value=[1990, 2010], className="dcc_control",
                    ),
                    html.P
                    (
                        "Filtro para fincas:", className="control_label"
                    ),
                    dbc.RadioItems
                    (
                        id="radio-fincas",
                        options=
                        [
                            {"label": "All", "value": 1},
                        ],
                    ),                
                    dcc.Dropdown
                    (
                        id="dropdown-categoria",
                        options=
                        [
                            {"label": col, "value": col} for col in ['florval','scarlet','qfc','ubate','la mana','santacruz','planicie','ajibe']
                        ],
                        multi=True,
                        value=['florval','scarlet','qfc','ubate','la mana','santacruz','planicie','ajibe'],
                        className="dcc_control",
                    ),
                ]
            ),    
            dbc.FormGroup
            (
                [
                    dbc.Label(u"Variedades"),
                    dbc.RadioItems
                    (
                        id="radio-variedades",
                        options=
                        [
                            {"label": "All", "value": 1},
                            {"label": "Claveles", "value": 2},
                            {"label": "Mini Claveles", "value": 3},
                        ],
                    ),
                    dcc.Dropdown
                    (
                        id="nivelCritica",
                        options=
                        [
                            {"label": col, "value": col}  for col in list_variedades
                        ],
                        multi=True,
                        value=list_variedades,
                        className="dcc_control",
                    )
                ]
            )
        ]
    )'''

'''def controls():
    return dbc.Card(
    [
        dbc.FormGroup(
            [
                html.P(
                            "Filtro por semana de la planta",
                            className="control_label",
                        ),
                dcc.RangeSlider(
                            id="year_slider",
                            min=1960,
                            max=2017,
                            value=[1990, 2010],
                            className="dcc_control",
                        ),
                html.P("Filtro para fincas:", className="control_label"),
        dbc.RadioItems(
                id="example-radios-row",
                options=[
                    {"label": "All", "value": 1},
                ],
            ),                
                dcc.Dropdown(
                    id="categoria",
                    options=[
                        {"label": col, "value": col} for col in ['florval','scarlet','qfc','ubate','la mana','santacruz','planicie','ajibe']
                    ],
                    multi=True,
                    value=['florval','scarlet','qfc','ubate','la mana','santacruz','planicie','ajibe'],
                    className="dcc_control",
                ),
            ]
        ),
        
        dbc.FormGroup(
            [
                dbc.Label(u"Variedades"),
        dbc.RadioItems(
                id="example-radios-row",
                options=[
                    {"label": "All", "value": 1},
                    {"label": "Claveles", "value": 2},
                    {"label": "Mini Claveles", "value": 3},
                ],
            ),
                dcc.Dropdown(
                    id="nivelCritica",
                    options=[
                        {"label": col, "value": col}  for col in list_variedades
                    ],
                    multi=True,
                    value=list_variedades,
                    className="dcc_control",
                ),
            ]
        )
    ],
    body=True,
)'''
'''

    # @app.callback(Output("nivelCritica3", "value"), [Input("example-radios-row", "value")])
    # def display_type(selector):
    #     if selector == 1:
    #         return ["prueba1","prueba2"]
    #     elif selector == 2:
    #         return ["GD", "GE", "GW", "IG", "IW", "OD", "OE", "OW"]
    #     elif selector == 3:
    #         return ["GD", "GE", "GW"]

def filters():
    return  html.Div(
        id="control-card",
        children=[
            html.P("Select Clinic"),
            dcc.Dropdown(
                id="clinic-select",
                options=[{"label": i, "value": i} for i in ['Subfiltro1','Subfiltro2']],
                value='Subfiltro1',
            ),
            html.Br(),
            html.P("Select Check-In Time"),
            dcc.DatePickerRange(
                id="date-picker-select",
                start_date='2014, 1, 1',
                end_date='2014, 1, 15',
                min_date_allowed='2014, 1, 1',
                max_date_allowed='2014, 12, 31',
                initial_visible_month='2014, 1, 1',
            ),
            html.Br(),
            html.Br(),
            html.P("Select Admit Source"),
            dcc.Dropdown(
                id="admit-select",
                options=[{"label": i, "value": i} for i in ['florval','scarlet','qfc','ubate','la mana','santacruz','planicie','ajibe']],
                value=['Subfiltro1','Subfiltro2'],
                multi=True,
            ),
            html.Br(),
            html.Div(
                id="reset-btn-outer",
                children=html.Button(id="reset-btn", children="Reset", n_clicks=0),
            ),
        ],
    )'''