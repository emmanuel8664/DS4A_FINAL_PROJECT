from components.data_access.data_access import data_access
from components.data_access.data_filter import Data_filter
import pandas as pd
class file_access(data_access):
    class __file_access:
        ruta_datos = r"D:\\Documentos\\Certificación DS4A\\Proyecto\\Git final\\DS4A_FINAL_PROJECT\\data"
        #ruta_datos = r"C:\\Users\\bolemm01\\Desktop\\Correlation1\\PROYECTO_FINAL\\data"
        ruta_estacion = ruta_datos + '\\estacion.csv'
        ruta_produccion = ruta_datos + '\\produccion_color.csv'
        ruta_finca = ruta_datos + '\\finca.csv'
        ruta_temperatura = ruta_datos + '\\temperatura.csv'
        ruta_radiacion = ruta_datos + '\\radiacion.csv'
        ruta_redes = ruta_datos + '\\result_nn2.csv'
        ruta_weather = ruta_datos + '\\weather.csv'
        #ruta_clima = ruta_datos + '\\clima.csv'
        def __init__(self):
            self.df_estacion = pd.read_csv(self.ruta_estacion, delimiter=',')
            self.df_produccion = pd.read_csv(self.ruta_produccion, delimiter=',',low_memory=False)
            self.df_finca = pd.read_csv(self.ruta_finca, delimiter=',',low_memory=False)
            self.df_temperatura = pd.read_csv(self.ruta_temperatura, delimiter=',',low_memory=False)
            self.df_radiacion = pd.read_csv(self.ruta_radiacion, delimiter=',',low_memory=False)
            self.df_redes = pd.read_csv(self.ruta_redes, delimiter=',', low_memory=False)
            self.df_weather = pd.read_csv(self.ruta_weather, delimiter=',', low_memory=False)
            self.df_clima = None
            #self.df_clima = pd.read_csv(self.ruta_clima, delimiter=',',low_memory=False)
            #data_finca = pd.read_csv(route+"\data\finca.csv", delimiter=',',low_memory=False)
            #print(self.df_produccion)
            self.data_filter = Data_filter()
        def realizar_filtro_fechas(self, df, fecha):
            rango_fechas = self.data_filter.get_rango_fechas()
            if rango_fechas['fecha_inicio']:
                if not df[df[fecha]>=rango_fechas['fecha_inicio']].empty:
                    df = df[df[fecha]>=rango_fechas['fecha_inicio']]
            if rango_fechas['fecha_fin']:
                if not df[df[fecha]<=rango_fechas['fecha_fin']].empty:
                    return df[df[fecha]<=rango_fechas['fecha_fin']]
                else:
                    return df
            else:
                return df
            #return df[(df[fecha]>=rango_fechas['fecha_inicio'])&(df[fecha]<=rango_fechas['fecha_fin'])]
        def realizar_filtro_fincas(self, df, finca):
            if not self.data_filter.get_fincas():
                return df
            else:
                return df[df[finca].isin(self.data_filter.get_fincas())]
        def realizar_filtro_colores(self, df, color):
            if not self.data_filter.get_colores():
                return df
            else:
                return df[df[color].isin(self.data_filter.get_colores())]
        def realizar_filtro_estaciones(self, df, estacion):
            if not self.data_filter.get_estaciones():
                return df
            else:
                return df[df[estacion].isin(self.data_filter.get_estaciones())]
        def realizar_filtro_estacion(self, df, estacion):
            if not self.data_filter.get_estacion():
                return df
            else:
                return df[df[estacion].isin(self.data_filter.get_estacion())]
        def realizar_filtro_variedades(self, df, variedad):
            if not self.data_filter.get_variedades():
                return df
            else:
                return df[df[variedad].isin(self.data_filter.get_variedades())]
        def get_df_estacion(self):
            return self.df_estacion
        def get_df_produccion(self):
            retorno = self.df_produccion.copy()
            retorno = self.realizar_filtro_fincas(retorno, 'finca')
            #retorno = self.realizar_filtro_estaciones(retorno, 'estacion')
            retorno = self.realizar_filtro_variedades(retorno, 'variedad')
            retorno = self.realizar_filtro_colores(retorno, 'Color')
            retorno = self.realizar_filtro_fechas(retorno, 'anosemana')
            return retorno
        def get_df_clima(self):
            return self.df_clima
        def get_df_finca(self):
            return self.df_finca
        def get_df_temperatura(self):
            retorno = self.df_temperatura.copy()
            retorno = self.realizar_filtro_fechas(retorno, 'Fecha')
            return retorno
        def get_df_radiacion(self):
            retorno = self.df_radiacion.copy()
            retorno = self.realizar_filtro_fechas(retorno, 'Fecha')
            return retorno
        def get_filtros_clima(self):
            retorno = {}
            retorno['estacion'] = self.data_filter.get_estacion()
            retorno['rango_clima'] = self.data_filter.get_rango_clima()
            return retorno
    instance = None
    def __init__(self):
        if not file_access.instance:
            file_access.instance = file_access.__file_access()
    def get_df_estacion(self):
        return self.instance.get_df_estacion()
    def get_df_produccion(self):
        return self.instance.get_df_produccion()
    def get_df_clima(self):
        return self.instance.get_df_clima()
    def get_df_finca(self):
        return self.instance.get_df_finca()
    def get_df_temperatura(self):     
        return self.instance.get_df_temperatura()
    def get_df_radiacion(self):
        return self.instance.get_df_radiacion()
    def get_df_redes(self):
        return self.instance.df_redes
    def get_df_weather(self):
        return self.instance.df_weather
    def get_filtros_clima(self):
        return self.instance.get_filtros_clima()
