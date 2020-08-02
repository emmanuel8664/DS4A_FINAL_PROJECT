from components.data_access.file_access import file_access
from pandas import pandas as pd


class neural_network():
    data_access = None
    def __init__(self):
        self.data_access = file_access()
    
    def neural_network():
        datos = self.data_access.get_df_produccion()
        datos.drop(['Bloque','Nave','Lado','Cama','Id Cama','Piloto/homogenea','Area','Suma de Indice tallos/M2','Suma de Indice tallos/planta','Notas'],axis=1,inplace=True)
        datos.rename({'Fecha Siembra':'fecha_siembra','Año Semana':'ano_semana','UP':'finca','Tipo':'tipo','Variedad':'variedad','Fecha siembra':'fecha_siembra','Concatenado':'concatenado','Tallos producidos':'tallos','Edad':'edad','Cantidad':'cantidad_plantas','Fiesta':'fiesta'},axis=1,inplace=True)
        datos['coeficiente']=datos['tallos']/datos['cantidad_plantas']
        datos['ano_semana']=datos['ano_semana'].astype(str)

        colores = self.data_access.get_df_variedad_color()
        colores.rename(columns={'Variedad':'variedad'},inplace=True)

        fechas= self.data_access.get_df_fechas()
        fechas['dia']=pd.to_datetime(fechas['dia'])
        semanas=fechas.groupby('ano_semana').max().reset_index()
        semanas['ano_semana']=semanas['ano_semana'].astype(str)

        estaciones = self.get_df_estacion()

        fincas=self.get_df_finca()
        fincas.rename(columns={'FINCAS':'nombre','SIGLA':'sigla','LATITUD':'latitud','LONGITUD':'longitud'},inplace=True)
        finca_estac = pd.DataFrame()

        for i in list(fincas.sigla.unique()):
            temp= fincas[fincas['sigla']==i]
            temp=pd.concat([temp,estaciones],ignore_index=True)
            temp['nombre']=temp.iloc[0,0]
            temp['sigla']=temp.iloc[0,1]
            temp['latitud']=temp.iloc[0,2]
            temp['longitud']=temp.iloc[0,3]
            temp.dropna(inplace=True)
            temp['distancia'] = np.sqrt((temp['LATITUD'] - temp['latitud'])**2 + (temp['LONGITUD'] - temp['longitud'])**2)
            temp.sort_values(['sigla','distancia'],ignore_index=True,inplace=True)
            temp=temp.head(1)
            finca_estac=pd.concat([finca_estac,temp])


        finca_estac=finca_estac.reset_index(drop=True)

        #Code for calculation of average points for every farm-variety-age-week
        promedio=pd.DataFrame(columns=('ansema','up','variedad','edad','indiceplan'))
        datos.ano_semana=datos.ano_semana.astype(int)
        for i in list(datos['ano_semana'].sort_values().unique()):
            desde = i-199
            datos_filt=datos[(datos['ano_semana']>=desde) & (datos['ano_semana']<i-4)].copy()
  
            curva_promed=datos_filt.groupby(['finca','variedad','edad'])['coeficiente'].mean().reset_index()
            curva_promed['ano_semana'] = i
            curva_promed['ano_semana'] = (curva_promed['ano_semana']).astype(str)  
            promedio=pd.concat([promedio,curva_promed],ignore_index=True)
            promedio=promedio.set_index(['ano_semana','finca','variedad','edad']).to_dict('index')

        def curva_promedio(ansem,up,variedad,edad):
            try:
              valor=promedio[ansem,up,variedad,edad]['coeficiente']
              return valor
            except:
            return 0
        datos.ano_semana=datos.ano_semana.astype(str)

        datos=datos.merge(semanas,on='ano_semana',how='left')
        datos['mes_dato']=datos.dia.dt.month     

        recons=datos.sort_values(['concatenado','edad']).reset_index(drop=True)

        lag_prod=10

        for i in tqdm(range(1,lag_prod+1)):
            strprod=str(i)+'sem_atras'
            strconc=str(i)+'concat_atras'
            recons[strprod]=recons['coeficiente'].shift(i)
            recons[strconc]=recons['concatenado'].shift(i)
            vald=str(i)+'valido'
            recons[vald]=recons.apply(lambda ff: 1 if ff[strconc]==ff['concatenado'] else 0,axis=1)
            recons[strprod]=recons.apply(lambda x: x[strprod] if x[vald]==1 else 0,axis=1)
            recons.drop(columns={strconc},inplace=True)
            recons.drop(columns={vald},inplace=True)

        recons.drop(columns={'Unnamed: 0'},inplace=True)
        recons=recons.merge(colores[['variedad','Color']],how='left',on='variedad')

        #agrega la columna de curva estandar para cada variedad-finca
        recons.ano_semana=(recons.ano_semana).astype(str)
        recons['curva_metodo_finca'] = recons.apply(lambda x: curva_promedio(x['ano_semana'],x['finca'],x['variedad'],x['edad']),axis=1)
        recons=recons[recons['tipo'].isin(['Minicarnation','Carnation'])]
        recons.Color.fillna('NoColor',inplace=True)
        recons['edad^2']=recons['edad']**2
        recons['edad^3']=recons['edad']**3


        #Red Neuronal
        consolidado_rn=pd.DataFrame()
        from sklearn.preprocessing import StandardScaler
        from tensorflow import keras
        from tensorflow.keras import layers
        recons=recons[recons['dia']>='01/01/2018']
        y_hat_rn=pd.Series(name='y_hat_falso')

        for i in recons.tipo.unique():
            for j in recons_test[recons_test['tipo']==i]['Color'].unique():
                temp_test=recons_test[(recons_test['tipo']==i)&(recons_test['Color']==j)]
                df_clean_test=pd.concat([temp_test[['edad','edad^2','edad^3','mes_dato','5sem_atras',
                                '6sem_atras','7sem_atras','8sem_atras','9sem_atras','10sem_atras',
                                 #'11sem_atras','12sem_atras','13sem_atras','14sem_atras','15sem_atras',
                                  'curva_metodo_finca','coeficiente']], pd.get_dummies(temp_test['variedad']), pd.get_dummies(temp_test['finca'])], axis=1)
                df_clean_test.fillna(value=0,inplace=True)
                y_real_test = df_clean_test.coeficiente
                X_real_test = df_clean_test.drop('coeficiente', axis=1)

                temp=recons[(recons['tipo']==i)&(recons['Color']==j)]
                temp=temp[temp['variedad'].isin(temp_test['variedad'].unique())]
                temp=temp[temp['finca'].isin(temp_test['finca'].unique())]
                df_clean=pd.concat([temp[['edad','edad^2','edad^3','mes_dato','5sem_atras',
                                 '6sem_atras','7sem_atras','8sem_atras','9sem_atras','10sem_atras',
                                  #'11sem_atras','12sem_atras','13sem_atras','14sem_atras','15sem_atras',
                                  'curva_metodo_finca','coeficiente']], pd.get_dummies(temp['variedad']), pd.get_dummies(temp['finca'])], axis=1)

                df_clean.fillna(value=0,inplace=True)
                y = df_clean.coeficiente
                X = df_clean.drop('coeficiente', axis=1)
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
                scaler = StandardScaler()
                X_train_std = pd.DataFrame(scaler.fit_transform(X_train), columns = X_train.columns)
                neurons = 256
                model = keras.Sequential([layers.Dense(neurons, activation='relu', input_shape=[len(X_train_std.columns)]),
                                  layers.Dense(neurons,activation='relu'),
                                  layers.Dense(1,activation='relu')])   #Capa salida
                model.compile(loss='mse', optimizer = 'adam')
                history = model.fit(X_train_std, y_train, epochs=100, validation_split = 0.2, verbose=0,batch_size=100)

                X_norm = scaler.transform(X_real_test)
                indice=X_real_test.reset_index()['index']
                y_hat=model.predict(X_norm)
                y_hat=pd.Series(y_hat[0:,0],name='y_hat')
                y_hat.index=X_real_test.index
                y_hat_rn=pd.concat([y_hat_rn,y_hat],axis=1)

        y_hat_rn.drop(columns={'y_hat_falso'},inplace=True)
        ser_y_hat=np.sum(y_hat_rn,axis=1)
        y_hat_rn['y_hat_red_n']=ser_y_hat
        validacion_y_hat=y_hat_rn[['y_hat_red_n']]
        validacion_final=pd.concat([recons_test,validacion_y_hat],axis=1)
                          