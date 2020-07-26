from components.data_access.data_access import data_access
import pandas as pd
class db_access(data_access):
    #ruta_datos = r"C:\\Users\\Usuario\\Documents\DS4A\\Project\\Proyecto\\Flower_production_forecast\\data"
    #ruta_estacion = ruta_datos + '\\estacion.csv'
    #ruta_produccion = ruta_datos + '\\estacion.csv'
    def __init__(self):
        pass
        #self.df_estacion = pd.read_csv(self.ruta_estacion, delimiter=',')
        #self.df_produccion = pd.read_csv(self.ruta_produccion, delimiter=',',low_memory=False)
        #data_clima = pd.read_csv(route+"\data\clima.csv", delimiter=',',low_memory=False)
        #data_finca = pd.read_csv(route+"\data\finca.csv", delimiter=',',low_memory=False)