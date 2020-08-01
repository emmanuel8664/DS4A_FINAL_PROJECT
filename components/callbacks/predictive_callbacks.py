from dash.dependencies import Input, Output
from components.data_access.data_filter import Data_filter
from components.views.predictive import *
#from components.tabs import *

data_filter = Data_filter()

def register_predictive_callbacks(app):
    # callback red neuronal
    @app.callback(
        Output('red_neuronal', 'figure'),
        [
            Input("predictive_date_filter0", "start_date"), 
            Input("predictive_date_filter0", "end_date"), 
            Input("predictive_farms_category0", "value"),
            Input("predictive_color_category0", "value")
        ]
    )
    def actualizar_red_neuronal(fecha_inicio, fecha_fin, finca, color):
        actualizar_fechas(fecha_inicio, fecha_fin)
        actualizar_finca(finca)
        actualizar_color(color)
        fig_red_neuronal = get_redes()
        return fig_red_neuronal
    
    # callback mapa de temperatura
    @app.callback(
        Output('predictive_temperatura', 'figure'),
        [
            Input("predictive_stations_category0", "value")
        ]
    )
    def actualizar_temperatura(estacion):
        actualizar_estacion(estacion)
        mapa_temperatura = get_temp2()
        return mapa_temperatura

def actualizar_fechas(fecha_inicio, fecha_fin):
    data_filter = Data_filter()
    data_filter.set_rango_fechas(fecha_inicio, fecha_fin)
def actualizar_finca(finca):
    data_filter = Data_filter()
    data_filter.set_finca(finca)
def actualizar_color(color):
    data_filter = Data_filter()
    data_filter.set_color(color)
def actualizar_estacion(estacion):
    data_filter = Data_filter()
    #data_filter.set_estacion(estacion)