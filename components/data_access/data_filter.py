class Data_filter:
    class __data_filter:
        def __init__(self):
            self.rangos_clima_aceptados = {1:'day',2:'Month'}
            self.abreviatura_fincas = {'florval': 'FV','la mana': 'LM','qfc': 'QF','scarlet': 'SC','santacruz': 'SZ','ubate': 'UB','planicie': 'PL','aljibe': 'AL'}
            self.claveles = ['Alicia','Bizet','Boiro','Brisa','Brut','Bubblicious','Caramel','Carole','Caronte','Cheerio','Country','Cowboy','CreamViana','Cris','Daniko','Diletta','DonPedro','Doncel','Farida','Fiesta','FiestaKomachi','Gioele','GioleCrema','Golem','GrandSlam','Hikran','Igloo','Jaffa','Komachi','KomachiBlanco','Mandalay','Megan','MerlettoCrimson','Minerva','Mizuki','Monalisa','Montoya','MoonLight','NobbioBurgundy','NobbioCherry','NobbioViolet','Novia','Olympia','Prinz','RedMagic','Soho','Solex','Sorriso','Tabasco','Trueno','VinoRosso','Virgilio','Voragine','Zafiro','Zenit','Zeppelin','10ST120°','C205°','Caribe°','Cervantes°','D63°','Extasis°','Hypnosis°','Jobin°','Jubilee°','Madrid°','Mohave°','Nobbioblackheart','Pelayo°','Selva°','Ulisse°','Carnation	Volare°']
            self.miniclaveles = ['Academy','Akari New','Aragon','Berry','Blanquita','Chateau','Cherry Tessino','Collin Lemon','Danny','Dino','Doobadoo','Dracula','Epsilon','Euforia','Fenix','Gold Strike','Green Tea','Ibis','Jester','Kim','Kinder','Lady','Laura','Lina','Masquerade','Merlot','Milkana','Nandi','Nimbus','Number One','Paranoya','Pearl Lady','Pigeon','Purple Sky','Purple Spectro','Rafflesia','Rosadita','Rosemary','Santos','Scarlette','Scooter','Selene','Skady','Spectro','Spitfire','Tasso','Tiger','Tokimeki','Vega','Vespa','Y 738','Bora bora°','C 736°','Golden Touch°','Ice Green*','Lollipop Pink°','Lollipop Violet°','Omelette°','Oscar°','PV50065°','Star Cherry Tessino','Xue°']
            self.rango_fechas = {'fecha_inicio': None, 'fecha_fin': None}
            self.colores = []
            self.variedades = []
            self.fincas = []
            self.rango_clima = self.rangos_clima_aceptados[2]
            self.estacion = 'acacias'
            self.finca = 'FV'
            self.color = 'DarkPink'
            self.variedad = None
            #self.finca = self.abreviatura_fincas['florval']
            #self.color = 'White'
        def get_rango_fechas(self):
            return self.rango_fechas
        def get_colores(self):
            return self.colores
        def get_color(self):
            return self.color
        def get_variedades(self):
            return self.variedades
        def get_variedad(self):
            return self.variedad    
        def get_estaciones(self):
            return [self.estacion]
        def get_estacion(self):
            return self.estacion
        def get_fincas(self):
            return self.fincas
        def get_finca(self):
            return self.finca
        def get_rango_clima(self):
            return self.rango_clima
        def set_rango_fechas(self, fecha_inicio, fecha_fin):
            self.rango_fechas['fecha_inicio'] = fecha_inicio
            self.rango_fechas['fecha_fin'] = fecha_fin
        def set_colores(self, colores):
            self.colores = colores
        def set_color(self, color):
            self.color = color
        def set_variedades(self, variedades):
            self.variedades = variedades
        def set_variedad(self, variedad):
            self.variedad = variedad    
        def set_estaciones(self, estaciones):
            self.estaciones = estaciones
        def set_estacion(self, estacion):
            self.estacion = estacion
        def set_fincas(self, fincas):
            self.fincas = fincas
        def set_finca(self, finca):
            self.finca = self.abreviatura_fincas[finca]
        def set_rango_clima(self, rango_clima):
            if rango_clima:
                self.rango_clima = self.rangos_clima_aceptados[rango_clima]
        def get_claveles(self):
            return self.claveles
        def get_miniclaveles(self):
            return self.miniclaveles
    instance = None
    def __init__(self):
        if not Data_filter.instance:
            Data_filter.instance = Data_filter.__data_filter()
    def get_rango_fechas(self):
        return self.instance.get_rango_fechas()
    def get_colores(self):
        return self.instance.get_colores()
    def get_color(self):
        return self.instance.get_color()
    def get_variedades(self):
        return self.instance.get_variedades()
    def get_variedad(self):
        return self.instance.get_variedad()    
    def get_estaciones(self):
        return self.instance.get_estaciones()
    def get_estacion(self):
        return self.instance.get_estacion()
    def get_fincas(self):
        return self.instance.get_fincas()
    def get_finca(self):
        return self.instance.get_finca()
    def get_rango_clima(self):
        return self.instance.get_rango_clima()
    def set_rango_fechas(self, fecha_inicio, fecha_fin):
        self.instance.set_rango_fechas(fecha_inicio, fecha_fin)
    def set_colores(self, colores):
        self.instance.set_colores(colores)
    def set_color(self, color):
        self.instance.set_color(color)
    def set_variedades(self, variedades):
        self.instance.set_variedades(variedades)
    def set_variedad(self, variedad):
        self.instance.set_variedad(variedad)    
    def set_estaciones(self, estaciones):
        self.instance.set_estaciones(estaciones)
    def set_estacion(self, estacion):
        self.instance.set_estacion(estacion)
    def set_fincas(self, fincas):
        self.instance.set_fincas(fincas)
    def set_finca(self, finca):
        self.instance.set_finca(finca)
    def set_rango_clima(self, rango_clima):
        self.instance.set_rango_clima(rango_clima)
    def get_claveles(self):
        return self.instance.get_claveles()
    def get_miniclaveles(self):
        return self.instance.get_miniclaveles()