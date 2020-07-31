from components.data_access.data_access import data_access
import pandas as pd
class file_access(data_access):
    class __file_access:
        #ruta_datos = r"C:\\Users\\Usuario\\Documents\DS4A\\Project\\Proyecto\\Flower_production_forecast\\data"
        ruta_datos = r"C:\\Users\\bolemm01\\Desktop\\Correlation1\\PROYECTO_FINAL\\data"
        ruta_estacion = ruta_datos + '\\estacion.csv'
        ruta_produccion = ruta_datos + '\\produccion_color.csv'
        ruta_finca = ruta_datos + '\\finca.csv'
        ruta_temperatura = ruta_datos + '\\temperatura.csv'
        ruta_radiacion = ruta_datos + '\\radiacion.csv'
        ruta_redes = ruta_datos + '\\result_nn1.csv'
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
            #self.df_clima = pd.read_csv(self.ruta_clima, delimiter=',',low_memory=False)
            #data_finca = pd.read_csv(route+"\data\finca.csv", delimiter=',',low_memory=False)
            #print(self.df_produccion)
    instance = None
    def __init__(self):
        if not file_access.instance:
            file_access.instance = file_access.__file_access()
    def get_df_estacion(self):
        return self.instance.df_estacion
    def get_df_produccion(self):
        return self.instance.df_produccion
    def get_df_clima(self):
        return self.instance.df_clima
    def get_df_finca(self):
        return self.instance.df_finca
    def get_df_temperatura(self):     
        return self.instance.df_temperatura
    def get_df_radiacion(self):
        return self.instance.df_radiacion
    def get_df_redes(self):
        return self.instance.df_redes
    def get_df_weather(self):
        return self.instance.df_weather
