from components.data_access.file_access import file_access
from pandas import pandas as pd

class descriptive_data():
    data_access = None
    eje_x = None
    eje_y = None
    def __init__(self):
        self.data_access = file_access()
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

    def get_prod_edad(self):
        df_production_edad = self.data_access.get_df_produccion()
        df = df_production_edad.groupby(['finca','edad'])['tallos_planta'].mean()
        df=df.add_suffix('').reset_index()
        return df

    def get_heatmap_temp_mean(self):

        filtros_temperaturas = self.data_access.get_filtros_clima()

        def hora_hora(x): return int(x[0:2]) 

        tem = self.data_access.get_df_temperatura()
        tem['Fecha'] = pd.to_datetime(tem['Fecha'])
        tem['Day_week']  = tem['Fecha'].dt.day_name()
        tem["Hora_single"] = tem["Hora"].apply(hora_hora)
        df_tem_mean_hora = tem.groupby(['Fecha','Day_week','Hora_single']).mean()
        
        estacion = filtros_temperaturas['estacion']
        filtro = filtros_temperaturas['rango_clima']

        df_tem_mean_hora_finca = df_tem_mean_hora.filter([estacion])
        dist = df_tem_mean_hora_finca.reset_index(level=[0,1,2])

        dist['Month_number']=dist['Fecha'].dt.month
        dist['Month'] = dist['Fecha'].dt.strftime('%B')
        dist['year'] = pd.DatetimeIndex(dist['Fecha']).year
        dist['day'] = dist['Fecha'].dt.day
        dist=dist.groupby([filtro,'Hora_single'])[estacion].mean()
        df = dist.to_frame()
        dist_df = df.reset_index(level=[0,1])
        dist_df['x'] = dist_df[filtro]
        dist_df['z'] = dist_df[estacion]
        return dist_df

    def get_heatmap_temp_min(self):

        filtros_temperaturas = self.data_access.get_filtros_clima()

        def hora_hora(x): return int(x[0:2]) 

        tem = self.data_access.get_df_temperatura()
        tem['Fecha'] = pd.to_datetime(tem['Fecha'])
        tem['Day_week']  = tem['Fecha'].dt.day_name()
        tem["Hora_single"] = tem["Hora"].apply(hora_hora)
        df_tem_min_hora = tem.groupby(['Fecha','Day_week','Hora_single']).min()
        
        estacion = filtros_temperaturas['estacion']
        filtro = filtros_temperaturas['rango_clima']

        df_tem_min_hora_finca = df_tem_min_hora.filter([estacion])
        dist = df_tem_min_hora_finca.reset_index(level=[0,1,2])

        dist['Month_number']=dist['Fecha'].dt.month
        dist['Month'] = dist['Fecha'].dt.strftime('%B')
        dist['year'] = pd.DatetimeIndex(dist['Fecha']).year
        dist['day'] = dist['Fecha'].dt.day
        dist=dist.groupby([filtro,'Hora_single'])[estacion].mean()
        df = dist.to_frame()
        dist_df = df.reset_index(level=[0,1])
        dist_df['x'] = dist_df[filtro]
        dist_df['z'] = dist_df[estacion]
        return dist_df
      
    def get_heatmap_temp_max(self):

        filtros_temperaturas = self.data_access.get_filtros_clima()

        def hora_hora(x): return int(x[0:2]) 

        tem = self.data_access.get_df_temperatura()
        tem['Fecha'] = pd.to_datetime(tem['Fecha'])
        tem['Day_week']  = tem['Fecha'].dt.day_name()
        tem["Hora_single"] = tem["Hora"].apply(hora_hora)
        df_tem_max_hora = tem.groupby(['Fecha','Day_week','Hora_single']).max()
        
        estacion = filtros_temperaturas['estacion']
        filtro = filtros_temperaturas['rango_clima']

        df_tem_max_hora_finca = df_tem_max_hora.filter([estacion])
        dist = df_tem_max_hora_finca.reset_index(level=[0,1,2])

        dist['Month_number']=dist['Fecha'].dt.month
        dist['Month'] = dist['Fecha'].dt.strftime('%B')
        dist['year'] = pd.DatetimeIndex(dist['Fecha']).year
        dist['day'] = dist['Fecha'].dt.day
        dist=dist.groupby([filtro,'Hora_single'])[estacion].mean()
        df = dist.to_frame()
        dist_df = df.reset_index(level=[0,1])
        dist_df['x'] = dist_df[filtro]
        dist_df['z'] = dist_df[estacion]
        return dist_df

    def get_heatmap_rad_mean(self):

        filtros_temperaturas = self.data_access.get_filtros_clima()

        def hora_hora(x): return int(x[0:2]) 

        tem = self.data_access.get_df_radiacion()
        tem['Fecha'] = pd.to_datetime(tem['Fecha'])
        tem['Day_week']  = tem['Fecha'].dt.day_name()
        tem["Hora_single"] = tem["Hora"].apply(hora_hora)
        df_tem_mean_hora = tem.groupby(['Fecha','Day_week','Hora_single']).mean()
        
        estacion = filtros_temperaturas['estacion']
        filtro = filtros_temperaturas['rango_clima']

        df_tem_mean_hora_finca = df_tem_mean_hora.filter([estacion])
        dist = df_tem_mean_hora_finca.reset_index(level=[0,1,2])
        dist['Month_number']=dist['Fecha'].dt.month


        dist['Month'] = dist['Fecha'].dt.strftime('%B')
        dist['year'] = pd.DatetimeIndex(dist['Fecha']).year
        dist['day'] = dist['Fecha'].dt.day
        dist=dist.groupby([filtro,'Hora_single'])[estacion].mean()
        df = dist.to_frame()
        dist_df = df.reset_index(level=[0,1])
        dist_df['x'] = dist_df[filtro]
        dist_df['z'] = dist_df[estacion]
        return dist_df