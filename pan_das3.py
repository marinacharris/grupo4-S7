import pandas as pd
try:
    df1 = pd.read_csv('surveys.csv')
except:
    print('error al leer el archivo')
else:
    print(df1)
    print(df1.head(10)) # imprime las primeras n lineas
    print(df1.tail(8)) # imprime la últimas n líneas
    print(df1.shape)
    print(df1.columns)
    print(pd.unique(df1['species_id'])) # retorna una lista con los valores únicos de una columna
    print(df1['species_id'].value_counts()) # cuenta la cantidad por valores únicos
    print(df1['weight'].describe()) # devuelve datos de estadística descriptiva
    print(df1['weight'].max())
    print(df1.groupby('species_id')['record_id'].count()['AH'])


#finally, se ejecuta independientemente de si el bloque try genera o no genera error
#else, se ejecuta si no se genera error




