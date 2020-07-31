class Data_filter:
    class __data_filter:
        def __init__(self):
            self.rangos_clima_aceptados = {1:'day',2:'Month'}
            self.rango_fechas = {'fecha_inicio': None, 'fecha_fin': None}
            self.colores = []
            self.variedades = []
            self.fincas = []
            self.rango_clima = self.rangos_clima_aceptados[2]
            self.estacion = 'acacias'
        def get_rango_fechas(self):
            return self.rango_fechas
        def get_colores(self):
            return self.colores
        def get_variedades(self):
            return self.variedades
        def get_estaciones(self):
            return [self.estacion]
        def get_estacion(self):
            return self.estacion
        def get_fincas(self):
            return self.fincas
        def get_rango_clima(self):
            return self.rango_clima
        def set_rango_fechas(self, fecha_inicio, fecha_fin):
            self.rango_fechas['fecha_inicio'] = fecha_inicio
            self.rango_fechas['fecha_fin'] = fecha_fin
        def set_colores(self, colores):
            self.colores = colores
        def set_variedades(self, variedades):
            self.variedades = variedades
        def set_estaciones(self, estaciones):
            self.estaciones = estaciones
        def set_estacion(self, estacion):
            self.estacion = estacion
        def set_fincas(self, fincas):
            self.fincas = fincas
        def set_rango_clima(self, rango_clima):
            if rango_clima:
                self.rango_clima = self.rangos_clima_aceptados[rango_clima]
            
    instance = None
    def __init__(self):
        if not Data_filter.instance:
            Data_filter.instance = Data_filter.__data_filter()
    def get_rango_fechas(self):
        return self.instance.get_rango_fechas()
    def get_colores(self):
        return self.instance.get_colores()
    def get_variedades(self):
        return self.instance.get_variedades()
    def get_estaciones(self):
        return self.instance.get_estaciones()
    def get_estacion(self):
        return self.instance.get_estacion()
    def get_fincas(self):
        return self.instance.get_fincas()
    def get_rango_clima(self):
        return self.instance.get_rango_clima()
    def set_rango_fechas(self, fecha_inicio, fecha_fin):
        self.instance.set_rango_fechas(fecha_inicio, fecha_fin)
    def set_colores(self, colores):
        self.instance.set_colores(colores)
    def set_variedades(self, variedades):
        self.instance.set_variedades(variedades)
    def set_estaciones(self, estaciones):
        self.instance.set_estaciones(estaciones)
    def set_estacion(self, estacion):
        self.instance.set_estacion(estacion)
    def set_fincas(self, fincas):
        self.instance.set_fincas(fincas)
    def set_rango_clima(self, rango_clima):
        self.instance.set_rango_clima(rango_clima)