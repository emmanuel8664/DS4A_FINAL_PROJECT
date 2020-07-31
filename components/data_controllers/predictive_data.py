from components.data_access.file_access import file_access
from pandas import pandas as pd

class predictive_data():
    data_access = None
    eje_x = None
    eje_y = None
    def __init__(self):
        self.data_access = file_access()

    def get_redes(self):
        df_redes = self.data_access.get_df_redes()

        finca='FV'
        color='DarkPink'
        fechaInicial='2019-06-01'

        data_produccion=df_redes[(df_redes['finca']==finca) & (df_redes['Color']==color) & (df_redes['dia']>=fechaInicial)]
        filter_dataset = data_produccion.copy()

        filter_dataset['%Cumplimiento_finca']= filter_dataset[' tallos_reales '].astype('float')/filter_dataset[' tallos_metodo_finca '].astype('float')
        filter_dataset['%Cumplimiento_red_neuronal']= filter_dataset[' tallos_reales '].astype('float')/filter_dataset[' tallos_red '].astype('float')
        
        filter_dataset = filter_dataset.filter(items=['dia','%Cumplimiento_finca','%Cumplimiento_red_neuronal'])
        filter_dataset['lim_inf']='0.95'
        filter_dataset['lim_sup']='1.15'

        return filter_dataset

    def get_temp(self):
        weather = self.data_access.get_df_weather()
        return weather


