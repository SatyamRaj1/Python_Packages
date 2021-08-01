import pandas as pd
import numpy as np
 #identifying and cleaning null values
print(pd.isnull(np.nan))  #isnull give true if therheck)e is null value(in bracket supplied a null value to c
print(pd.notnull(np.nan))  #opposite of isnull
print(np.isinf(np.inf))  #check infinte value
print(np.isfinite(np.inf))  #opposit

a = np.array([1, 2, 3, np.nan, np.nan, 4])
print(a[np.isfinite(a)].sum())   #sum of all finite
print(pd.isnull(pd.Series([1,4,np.nan,767])))
dt=pd.DataFrame({
    'Column A':[5,8,987,76],
    'Column B':[76,np.nan,76,8],
    'Column C':[6.67,None,765,8]})
s=pd.Series([1, 2, 3, np.nan, np.nan, 4])
print(pd.isnull(dt))
print(pd.isnull(dt).count())
print(s[s.notnull()])   #print not null values   M2 print(s[s.notnull()])

#if only to select non null value
#Dropping
print(s.dropna())
print(dt.isnull().sum())   #number of null values column wise
print(dt.dropna())  #drop any row which has atleast 1 null
print(dt.dropna(axis=1))  #column wise

#dropna with conditions
print(dt.dropna(how='all'))  #if all values are null
print(dt.dropna(how='any'))
print(dt.dropna(thresh=2))  #if min 2 null values
print(dt.dropna(thresh=2, axis='columns'))


#filling null values
print(s.fillna(0))
print(s.fillna(s.mean()))
print(s.fillna(method='ffill'))#fill value to nnull just above it  #if null at beginning then it remain null
print(s.fillna(method='bfill'))  # fill value to nnull just below it
#work for dataframes too (row and column wise)


#cleaning not null values
a=pd.DataFrame({
    'Sex':['M','F','M','D','?'],
    'Age':[29,30,24,294,25]})
print(a['Sex'].unique())         #all unique enteries
print(a['Sex'].value_counts())    #no. of each enteries
print(a['Sex'].replace('D','F'))  #replace D by F
print(a['Sex'].replace({'D':'F','?':'M'}))
print(a['Sex'].replace('D','F'))
print(a.replace({
    'Sex':{
        'D':'F',
        '?':'M'
        },
    'Age':{
        294:32
        }}))
a.loc[a['Age']>100,'Age']=a.loc[a['Age']>100,'Age']/10   #divide age if >100
print(a)
#duplicate values
amb= pd.Series([
    'France',
    'United Kingdom',
    'United Kingdom',
    'Italy',
    'Germany',
    'Germany',
    'Germany',
], index=[
    'Gérard Araud',
    'Kim Darroch',
    'Peter Westmacott',
    'Armando Varricchio',
    'Peter Wittig',
    'Peter Ammon',
    'Klaus Scharioth '
])
print(amb.duplicated())  #print true if duplicate (not first one)  #by default
print(amb.duplicated(keep='last'))  #tprint true if duplicate (not last one)  #start from down
print(amb.duplicated(keep=False))  #print all duplicate true
print(amb.drop_duplicates())  #drop duplicate
print(amb.drop_duplicates(keep='last'))  #all 3similiar to duplicate

#dataframe
pl = pd.DataFrame({
    'Name': [
        'Kobe Bryant',
        'LeBron James',
        'Kobe Bryant',
        'Carmelo Anthony',
        'Kobe Bryant',
    ],
    'Pos': [
        'SG',
        'SF',
        'SG',
        'SF',
        'SF'
    ]
})
print(pl)
print(pl.duplicated())  #if completely duplicate
print(pl.duplicated(subset=['Name'])) #by name
print(pl.duplicated(subset=['Name'],keep='last'))
print(pl.drop_duplicates(subset=['Name']))  #dropping

#text handling
#splitting
df = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I  T_2'
]})

print(df['Data'].str.split('_'))  #date type have dt, category cat, string str
df=df['Data'].str.split('_',expand=True)  #expand to create in dataframe format
df.columns=['Year','Sex','Country','No. of children']
print(df)
print(df['Year'].str.contains('\?'))#\ to escape as ? has especial meaning
print(df['Country'].str.contains('U'))
print(df['Country'].str.strip())  #select only one column
print(df['Country'].str.replace('  ',''))




