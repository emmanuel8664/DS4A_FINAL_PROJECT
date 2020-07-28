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
                            id="date_filter"+str(id),
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
                    ),
                    dbc.FormGroup(
                        [
                            html.P("Filtro para estaciones:", className="control_label"),
                            dbc.RadioItems(id="radio-estaciones"+str(id),options=[{"label": "Día", "value": 1},{"label": "Mes", "value": 2}],),                
                            dcc.Dropdown(id="categoria-estaciones"+str(id),options=[{"label": col, "value": col} for col in ['acacias', 'aljibe', 'cipres']],multi=False,value='aljibe',className="dcc_control",),
                           
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


