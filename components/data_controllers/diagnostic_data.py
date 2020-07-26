from components.data_access.file_access import file_access


class diagnostic_data():
    data_access = None
    eje_x = None
    eje_y = None
    def __init__(self):
        self.data_access = file_access()
    def get_bar(self):
        df_produccion = self.data_access.get_df_produccion()
        #df_production.rename(columns=variables, inplace=True)
        #curvas = df_production.groupby(['finca','variedad','edad']).agg({'tallos_planta':['mean','median']}).reset_index()
        curvas = df_produccion.groupby('finca').agg({'tallosproducidos':'count'}).reset_index().sort_values('tallosproducidos', ascending = False)
        #curvas[(curvas.finca == 'SC') & (curvas.variedad == 'Alicia')].plot(x='edad', y = 'tallos_planta', figsize=(15,7), title = 'SC'+' - '+'Alicia')
        #df.groupby('finca').agg({'tallos_planta':['count']}).reset_index()
        #print(df)
        self.actualizar_ejes('finca','tallosproducidos')
        return curvas
    def get_line(self):
        df_produccion = self.data_access.get_df_produccion()
        curvas = df_produccion.groupby('finca').agg({'tallosproducidos':'count'}).reset_index()
        self.actualizar_ejes('finca','tallosproducidos')
        return curvas
    def get_boxplot(self):
        df_produccion = self.data_access.get_df_produccion()
        curvas = df_produccion.groupby(['finca','variedad','edad']).agg({'tallos_planta':['mean','median']}).reset_index()
        self.actualizar_ejes('edad','tallos_planta')
        return curvas
    def get_scatter(self):
        df_produccion = self.data_access.get_df_produccion()
        curvas = df_produccion.groupby(['finca','variedad','edad']).agg({'tallos_planta':['mean','median']}).reset_index()
        self.actualizar_ejes('edad','tallos_planta')
        return curvas

    def actualizar_ejes(self, eje_x, eje_y):
        self.eje_x = eje_x
        self.eje_y = eje_y
    def get_eje_x(self):
        return self.eje_x
    def get_eje_y(self):
        return self.eje_y