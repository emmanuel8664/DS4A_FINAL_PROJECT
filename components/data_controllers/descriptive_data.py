from components.data_access.file_access import file_access
from pandas import pandas as pd

class descriptive_data():
    data_access = None
    eje_x = None
    eje_y = None
    def __init__(self):
        self.data_access = file_access()
    def get_hist(self):
        df_production = self.data_access.get_df_produccion()
        #df_production.rename(columns=variables, inplace=True)
        curvas = df_production.groupby(['finca','variedad','edad']).agg({'tallos_planta':['mean','median']}).reset_index()
        #curvas[(curvas.finca == 'SC') & (curvas.variedad == 'Alicia')].plot(x='edad', y = 'tallos_planta', figsize=(15,7), title = 'SC'+' - '+'Alicia')
        #df.groupby('finca').agg({'tallos_planta':['count']}).reset_index()
        #print(df)
        self.actualizar_ejes('edad','tallos_planta')
        return curvas
    def get_map(self):
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
        df['text'] = df['name'] + '<br>Population ' + (df['pop']/1e6).astype(str)+' million'
        return df
    def actualizar_ejes(self, eje_x, eje_y):
        self.eje_x = eje_x
        self.eje_y = eje_y
    def get_eje_x(self):
        return self.eje_x
    def get_eje_y(self):
        return self.eje_y

    def get_map2(self):
        df_production_map = self.data_access.get_df_produccion()
        df_fincas_map = self.data_access.get_df_finca()

        df_production_map_2=df_production_map.groupby('finca')['tallos_planta'].mean()
        df_production_map_2=df_production_map_2.add_suffix('').reset_index()
        df_production_map_2=df_production_map_2.sort_values(by=['finca'])

        df_fincas_map2 = df_fincas_map.sort_values(by=['finca']).reset_index()
        
        result = pd.concat([df_production_map_2,df_fincas_map2], axis=1, join='inner')
        result2 = result.loc[:,~result.columns.duplicated()]
        return result2