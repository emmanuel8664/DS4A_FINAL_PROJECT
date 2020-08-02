from dash.dependencies import Input, Output
from components.data_access.data_filter import Data_filter
from components.views.descriptive import *
#from components.tabs import *

data_filter = Data_filter()

def register_descriptive_callbacks(app):
    # callback figura producción vs edad
    @app.callback(
        Output('fig_desc_prod_edad', 'figure'),
        [
            Input("date_filter0", "start_date")
            , Input("date_filter0", "end_date")
            , Input("categoria0", "value")
            , Input("categoria-color0", "value")
            , Input("nivelCritica0", "value")
        ]
    )
    def actualizar_figura_produccion(fecha_inicio, fecha_fin, fincas, colores, variedades):
        actualizar_fechas(fecha_inicio, fecha_fin)
        actualizar_fincas(fincas)
        actualizar_colores(colores)
        actualizar_variedades(variedades)
        fig_desc_prod_edad = get_prod_edad()
        return fig_desc_prod_edad
    # callback mapa de fincas
    @app.callback(
        Output('mapFincas', 'srcDoc'),
        [
            Input("date_filter0", "start_date")
            , Input("date_filter0", "end_date")
            , Input("categoria0", "value")
            , Input("categoria-color0", "value")
            , Input("nivelCritica0", "value")
        ]
    )
    def actualizar_mapa_calor(fecha_inicio, fecha_fin, fincas, colores, variedades):
        actualizar_fechas(fecha_inicio, fecha_fin)
        actualizar_fincas(fincas)
        actualizar_colores(colores)
        actualizar_variedades(variedades)
        get_map2()
        mapFincas = open(ruta_datos+'\\mymap.html', 'r').read()
        return mapFincas
    
    # callback mapa de calor de temperatura máxima
    @app.callback(
        Output('heatmap_temp_max', 'figure'),
        [
            Input("date_filter0", "start_date"), 
            Input("date_filter0", "end_date"), 
            Input("radio-estaciones0", "value"),
            Input("categoria-estaciones0", "value")
        ]
    )
    def actualizar_mapa_calor_temp_max(fecha_inicio, fecha_fin, radio_estaciones, estacion):
        actualizar_fechas(fecha_inicio, fecha_fin)
        actualizar_rango_clima(radio_estaciones)
        actualizar_estacion(estacion)
        mapFincas = get_heatmap_temp_max()
        return mapFincas

    # callback mapa de calor de temperatura media
    @app.callback(
        Output('heatmap_temp_mean', 'figure'),
        [
            Input("date_filter0", "start_date"), 
            Input("date_filter0", "end_date"), 
            Input("radio-estaciones0", "value"),
            Input("categoria-estaciones0", "value")
        ]
    )
    def actualizar_mapa_calor_temp_mean(fecha_inicio, fecha_fin, radio_estaciones, estacion):
        actualizar_fechas(fecha_inicio, fecha_fin)
        actualizar_rango_clima(radio_estaciones)
        actualizar_estacion(estacion)
        mapFincas = get_heatmap_temp_mean()
        return mapFincas

    # callback mapa de calor de temperatura mínima
    @app.callback(
        Output('heatmap_temp_min', 'figure'),
        [
            Input("date_filter0", "start_date"), 
            Input("date_filter0", "end_date"), 
            Input("radio-estaciones0", "value"),
            Input("categoria-estaciones0", "value")
        ]
    )
    def actualizar_mapa_calor_temp_min(fecha_inicio, fecha_fin, radio_estaciones, estacion):
        actualizar_fechas(fecha_inicio, fecha_fin)
        actualizar_rango_clima(radio_estaciones)
        actualizar_estacion(estacion)
        mapFincas = get_heatmap_temp_min()
        return mapFincas

    # callback mapa de calor de radiación media
    @app.callback(
        Output('heatmap_rad_mean', 'figure'),
        [
            Input("date_filter0", "start_date"), 
            Input("date_filter0", "end_date"), 
            Input("radio-estaciones0", "value"),
            Input("categoria-estaciones0", "value")
        ]
    )
    def actualizar_mapa_calor_rad_mean(fecha_inicio, fecha_fin, radio_estaciones, estacion):
        actualizar_fechas(fecha_inicio, fecha_fin)
        actualizar_rango_clima(radio_estaciones)
        actualizar_estacion(estacion)
        mapFincas = get_heatmap_rad_mean()
        return mapFincas

    # callback mapa de calor de radiación media
    @app.callback(
        Output('nivelCritica0', 'value'),
        [
            Input("radio-variedades0", "value")
        ]
    )
    def actualizar_filtro_variedades(radio_variedades):
        data_filter = Data_filter()
        if radio_variedades == 3:
            return data_filter.get_miniclaveles()
        elif radio_variedades == 2:
            return data_filter.get_claveles()
        else:
            return data_filter.get_miniclaveles() + data_filter.get_claveles()

def actualizar_fechas(fecha_inicio, fecha_fin):
    data_filter = Data_filter()
    data_filter.set_rango_fechas(fecha_inicio, fecha_fin)
def actualizar_fincas(fincas):
    data_filter = Data_filter()
    data_filter.set_fincas(fincas)
def actualizar_colores(colores):
    data_filter = Data_filter()
    data_filter.set_colores(colores)
def actualizar_variedades(variedades):
    data_filter = Data_filter()
    data_filter.set_variedades(variedades)
def actualizar_rango_clima(rango_clima):
    data_filter = Data_filter()
    data_filter.set_rango_clima(rango_clima)
def actualizar_estacion(estacion):
    data_filter = Data_filter()
    data_filter.set_estacion(estacion)
