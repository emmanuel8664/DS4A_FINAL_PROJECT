from dash.dependencies import Input, Output
from components.data_access.data_filter import Data_filter
from components.views.predictive import *
#from components.tabs import *

data_filter = Data_filter()

def register_predictive_callbacks(app):
    # callback gráfica cumplimiento red neuronal
    @app.callback(
        Output('red1', 'figure'),
        [
            #Input("predictive_date_filter0", "start_date"), 
            Input("predictive_date_filter0", "end_date"), 
            Input("predictive_farms_category0", "value"),
            Input("predictive_color_category0", "value"),
            Input("radio_predictive_varieties0", "value")
        ]
    )
    def actualizar_grafica_cumplimiento(fecha_fin, finca, color, tipo_variedad):
        actualizar_fechas('2019-06-01', fecha_fin)
        actualizar_finca(finca)
        actualizar_color(color)
        actualizar_tipo_variedad(tipo_variedad)
        figura = get_redes()
        return figura
    
    # callback gráfica cumplimiento red neuronal
    @app.callback(
        Output('red2', 'figure'),
        [
            Input("predictive_farms_category0", "value"),
            Input("predictive_color_category0", "value"),
            Input("radio_predictive_varieties0", "value")
        ]
    )
    def actualizar_grafica_pronostico(finca, color, tipo_variedad):
        actualizar_finca(finca)
        actualizar_color(color)
        actualizar_tipo_variedad(tipo_variedad)
        figura = get_pronostico()
        return figura
    
    # callback mapa de cambio de temperatura
    @app.callback(
        Output('temperatura1', 'figure'),
        [
            Input("predictive_stations_category0", "value")
        ]
    )
    def actualizar_cambio_temperatura(estacion):
        actualizar_estacion(estacion)
        figura = get_temp()
        return figura

    # callback lineplot de cambio de temperatura
    @app.callback(
        Output('temperatura2', 'figure'),
        [
            Input("predictive_stations_category0", "value")
        ]
    )
    def actualizar_temperatura_lineplot(estacion):
        actualizar_estacion(estacion)
        figura = get_temp2()
        return figura

    # callback figura viento
    @app.callback(
        Output('wind', 'figure'),
        [
            Input("predictive_stations_category0", "value")
        ]
    )
    def actualizar_viento(estacion):
        actualizar_estacion(estacion)
        figura = get_wind()
        return figura

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
    data_filter.set_estacion(estacion)

def actualizar_tipo_variedad(tipo_variedad):
    data_filter = Data_filter()
    if tipo_variedad == 1:
        data_filter.set_variedad('Carnation')
    elif tipo_variedad == 2:
        data_filter.set_variedad('Minicarnation')    