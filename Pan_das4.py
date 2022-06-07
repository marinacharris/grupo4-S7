import pandas as pd 
df1 = pd.read_csv('surveys.csv')
df2 = df1['month']
print(df2, type(df2))
df3 = df1[['species_id', 'plot_id']]
print(df3, type(df3))
print(df1[15:26])
print(df1.iloc[0:4,1:3])
print(df1.iloc[[2,4,6],1:4])
print(df1[df1.year==1985])
print(df1[(df1.year>=1985) & (df1.year<=1990) ]) #and:&, or:|, not:~

