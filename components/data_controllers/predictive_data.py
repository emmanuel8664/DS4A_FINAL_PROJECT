from components.data_access.file_access import file_access
from pandas import pandas as pd

class predictive_data():
    data_access = None
    eje_x = None
    eje_y = None
    def __init__(self):
        self.data_access = file_access()

    def get_max_data(self):
        data_proyeccion = self.data_access.get_df_redes()
        max_data = data_proyeccion['dia'].max()
        return max_data

    def get_redes(self):
        data_produccion = self.data_access.get_df_redes()






        
        # finca = 'FV'
        # color = 'DarkPink'

        data_produccion=data_produccion[data_produccion['dia']>='2019-06-01']

        

        filter_dataset = data_produccion.copy()

        filter_dataset['%Cumplimiento_finca']= filter_dataset[' tallos_reales '].astype('float')/filter_dataset[' tallos_metodo_finca '].astype('float')
        filter_dataset['%Cumplimiento_red_neuronal']= filter_dataset[' tallos_reales '].astype('float')/filter_dataset[' tallos_red '].astype('float')
        
        filter_dataset = filter_dataset.filter(items=['dia','%Cumplimiento_finca','%Cumplimiento_red_neuronal'])
        filter_dataset['lim_inf']='0.95'
        filter_dataset['lim_sup']='1.15'

        return filter_dataset

    def get_temp(self):
        weather = self.data_access.get_df_estaciones_pronostico()
        #finca = 'aljibe'
        #weather2=weather[weather['finca']==finca]
        return weather

    def convert(self,d):
        dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
        ix = round(d / (360. / len(dirs)))
        return dirs[ix % len(dirs)]

    def f(self,row):
        if ((row['list__wind__speed']>=0) & (row['list__wind__speed']<=0.5)):
            val = '0.0-0.5'
        elif ((row['list__wind__speed']>0.5) & (row['list__wind__speed']<=1.0)):
            val = '0.5-1.0'
        elif ((row['list__wind__speed']>1.0) & (row['list__wind__speed']<=1.5)):
            val = '1.0-1.5'
        elif ((row['list__wind__speed']>1.5) & (row['list__wind__speed']<=2.0)):
            val = '1.5-2.0'
        elif ((row['list__wind__speed']>2.0) & (row['list__wind__speed']<=2.5)):
            val = '2.0-2.5'
        else:
            val = '>2.5'
        return val      

    def get_wind(self):
        weather = self.data_access.get_df_estaciones_pronostico()
        #finca='aljibe'
        #weather2 = weather[weather['finca']==finca]
        lista =[]
        for index, row in weather.iterrows():
            a=self.convert(row['list__wind__deg'])
            lista.append(a)
        weather['direction']=lista
        weather['range']=weather.apply(self.f, axis=1)
        weather2=weather.groupby(['direction','range'])['range'].count()\
        .reset_index(name="count")  
        return weather2

    def get_proyeccion(self):
        data = self.data_access.get_df_proyeccion()
        pronostico = data.groupby(['dia','finca','Color']).agg({'tallos_metodo_finca':'sum','tallos_red':'sum'}).reset_index() 
        return pronostico