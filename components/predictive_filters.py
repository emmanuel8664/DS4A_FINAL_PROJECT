import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd

from components.data_access.file_access import file_access

class Predictive_filter:
    class __predictive_filter:
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

            data_estaciones = data_access.get_df_estacion()
            
            list_dates = np.sort(data_produccion['anosemana'].unique())
            list_dates_converted = pd.to_datetime(list_dates)
            initial_value = list_dates_converted[0]
            last_value = list_dates_converted[len(list_dates_converted)-1]


            temperatura = data_access.get_df_temperatura()
            estaciones = temperatura.columns[2:-2]
            estacion = data_access.get_filtros_clima()['estacion']


            type_flowers = ["All ", "Carnations", "Mini Carnations"]
            filtro = dbc.Card(
                [
                    dbc.FormGroup(
                        [
                            html.P("Date",className="control_label"),
                            dcc.DatePickerRange(
                            id="predictive_date_filter"+str(id),
                            start_date_placeholder_text="Start Date",
                            end_date_placeholder_text="End Date",
                            start_date = '2019-06-01',
                            #clearable=True,
                            #with_portal=True,
                            calendar_orientation='vertical',)  
                        ]
                    ),
                     dbc.FormGroup(
                        [
                            html.P("Farms:", className="control_label"),
                            #dbc.RadioItems(id="radio-fincas"+str(id),options=[{"label": "All", "value": 1},],),                
                            dcc.Dropdown(id="predictive_farms_category"+str(id),options=[{"label": col, "value": col} for col in list_fincas],value='florval',className="dcc_control",),
                           
                        ]
                    ),
                     dbc.FormGroup(
                        [
                            html.P("Colors:", className="control_label"),
                            #dbc.RadioItems(id="radio-color"+str(id),options=[{"label": "All", "value": 1},],),                
                            dcc.Dropdown(id="predictive_color_category"+str(id),options=[{"label": col, "value": col} for col in list_colors_without_nan],value='DarkPink',className="dcc_control",),
                           
                        ]
                    ),
                    dbc.Label(u"Varieties"),
                            dbc.RadioItems(
                                id="radio_predictive_varieties"+str(id),
                                options=[
                                    {"label": "Carnations", "value": 1},
                                    {"label": "Mini Carnations", "value": 2},
                                ],
                                value = 1
                            ),
                    dbc.FormGroup(
                        [
                            html.P("Weather Stations:", className="control_label"),
                            dcc.Dropdown(id="predictive_stations_category"+str(id),options=[{"label": col, "value": col} for col in estaciones],multi=False,value=estacion,className="dcc_control",)
                        ]
                    )
                ],
                body=True,
            )
            self.filtros.append(filtro)
    instance = None
    def __init__(self):
        if not self.instance:
            self.instance = self.__predictive_filter()
    def get_filtro(self):
        return self.instance.get_filtro()
    #def __getattribute__(self, name):
        #return getattr(self.instance, name)


#from components.data_load import *


