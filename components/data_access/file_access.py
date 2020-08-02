from components.data_access.data_access import data_access
from components.data_access.data_filter import Data_filter
import pandas as pd

class file_access(data_access):
    class __file_access:
        #ruta_datos = r"D:\\Documentos\\Certificación DS4A\\Proyecto\\Git final\\Por unir\\2\\DS4A_FINAL_PROJECT\\data"
        ruta_datos = r"C:\\Users\\bolemm01\\OneDrive - CSG Systems Inc\\Desktop\\DS4A\\DS4A_COPY\\DS4A_FINAL_PROJECT\\data"
        ruta_estacion = ruta_datos + '\\estacion.csv'
        ruta_produccion = ruta_datos + '\\produccion_color.csv'
        ruta_finca = ruta_datos + '\\finca.csv'
        ruta_temperatura = ruta_datos + '\\temperatura.csv'
        ruta_radiacion = ruta_datos + '\\radiacion.csv'
        ruta_redes = ruta_datos + '\\result_nn1.csv'
        ruta_weather = ruta_datos + '\\weather.csv'
        ruta_estaciones_pronostico = ruta_datos + '\\estaciones_pronostico.csv'
        ruta_pronostico = ruta_datos + '\\resultado_final.csv'
        ruta_colores = ruta_datos + '\\variedad_color.xlsx'
        ruta_fechas = ruta_datos + '\\fechas.xlsx'
        #ruta_clima = ruta_datos + '\\clima.csv'
        def __init__(self):
            self.df_estacion = pd.read_csv(self.ruta_estacion, delimiter=',')
            self.df_produccion = pd.read_csv(self.ruta_produccion, delimiter=',',low_memory=False)
            self.df_finca = pd.read_csv(self.ruta_finca, delimiter=',',low_memory=False)
            self.df_temperatura = pd.read_csv(self.ruta_temperatura, delimiter=',',low_memory=False)
            self.df_radiacion = pd.read_csv(self.ruta_radiacion, delimiter=',',low_memory=False)
            self.df_redes = pd.read_csv(self.ruta_redes, delimiter=',', low_memory=False)
            self.df_estaciones_pronostico = pd.read_csv(self.ruta_estaciones_pronostico, delimiter=',',low_memory=False)
            self.df_proyeccion = pd.read_csv(self.ruta_pronostico, delimiter=',', low_memory=False)
            self.df_variedad_color = pd.read_excel(self.ruta_colores)
            self.df_fechas = pd.read_excel(self.ruta_fechas)
            self.df_clima = None
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
        def realizar_filtro_fincas(self, df, finca):
            if not self.data_filter.get_fincas():
                return df
            else:
                return df[df[finca].isin(self.data_filter.get_fincas())]
        def realizar_filtro_finca(self, df, finca):
            if not self.data_filter.get_finca():
                return df
            else:
                return df[df[finca].isin([self.data_filter.get_finca()])]
        def realizar_filtro_colores(self, df, color):
            if not self.data_filter.get_colores():
                return df
            else:
                return df[df[color].isin(self.data_filter.get_colores())]
        def realizar_filtro_color(self, df, color):
            if not self.data_filter.get_color():
                return df
            else:
                return df[df[color].isin([self.data_filter.get_color()])]
        def realizar_filtro_estaciones(self, df, estacion):
            if not self.data_filter.get_estaciones():
                return df
            else:
                return df[df[estacion].isin(self.data_filter.get_estaciones())]
        def realizar_filtro_estacion(self, df, estacion):
            if not self.data_filter.get_estacion():
                return df
            else:
                return df[df[estacion].isin([self.data_filter.get_estacion()])]
        def realizar_filtro_variedades(self, df, variedad):
            if not self.data_filter.get_variedades():
                return df
            else:
                return df[df[variedad].isin(self.data_filter.get_variedades())]
        def realizar_filtro_variedad(self, df, variedad):
            if not self.data_filter.get_variedad():
                return df
            else:
                return df[df[variedad].isin([self.data_filter.get_variedad()])]       
        def get_df_estacion(self):
            return self.df_estacion
        def get_df_produccion(self):
            retorno = self.df_produccion.copy()
            retorno = self.realizar_filtro_fincas(retorno, 'finca')
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
        def get_df_redes(self):
            retorno = self.df_redes.copy()
            retorno = self.realizar_filtro_fechas(retorno, 'dia')
            retorno = self.realizar_filtro_finca(retorno, 'finca')
            retorno = self.realizar_filtro_color(retorno, 'Color')
            return retorno
        def get_filtros_clima(self):
            retorno = {}
            retorno['estacion'] = self.data_filter.get_estacion()
            retorno['rango_clima'] = self.data_filter.get_rango_clima()
            return retorno
        def get_lista_variedades(self, tipo_filtro):
            if tipo_filtro == 3:
                retorno = self.data_filter.get_miniclaveles()
            elif tipo_filtro == 2:
                retorno = self.data_filter.get_claveles()
            else:
                retorno = self.data_filter.get_miniclaveles() + self.data_filter.get_claveles()
            return retorno
        def get_lista_variedades_produccion(self, tipo_filtro):
            retorno = self.get_df_produccion()
            retorno = retorno['variedad'].isin(self.get_lista_variedades(tipo_filtro))['variedad'].unique()
            return retorno
        def get_df_proyeccion(self):
            retorno = self.df_proyeccion.copy()
            retorno = self.realizar_filtro_fechas(retorno, 'dia')
            retorno = self.realizar_filtro_finca(retorno, 'finca')
            retorno = self.realizar_filtro_color(retorno, 'Color')
            retorno = self.realizar_filtro_variedad(retorno, 'tipo')
            return retorno
        def get_df_estaciones_pronostico(self):
            retorno = self.df_estaciones_pronostico.copy()
            retorno = self.realizar_filtro_estacion(retorno, 'finca')
            return retorno
    instance = None
    def __init__(self):
        if not file_access.instance:
            file_access.instance = file_access.__file_access()
    def get_df_estacion(self):
        return self.instance.get_df_estacion()
    def get_df_produccion(self):
        return self.instance.get_df_produccion()
    def get_lista_variedades_produccion(self, tipo_filtro):
        return self.instance.get_lista_variedades_produccion(tipo_filtro)
    def get_df_clima(self):
        return self.instance.get_df_clima()
    def get_df_finca(self):
        return self.instance.get_df_finca()
    def get_df_temperatura(self):     
        return self.instance.get_df_temperatura()
    def get_df_radiacion(self):
        return self.instance.get_df_radiacion()
    def get_df_redes(self):
        return self.instance.get_df_redes()
    def get_filtros_clima(self):
        return self.instance.get_filtros_clima()
    def get_df_proyeccion(self):
        return self.instance.get_df_proyeccion()
    def get_df_estaciones_pronostico(self):
        return self.instance.get_df_estaciones_pronostico()
    def get_df_variedad_color(self):
        return self.instance.get_df_variedad_color()
    def get_df_fechas(self):
        return self.instance.get_df_fechas()    
