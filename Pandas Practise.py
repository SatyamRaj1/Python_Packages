import pandas as pd
import numpy as np
'''
s=pd.Series([1,2,3,4,5,6,np.nan,8,45,10])  #np.nan creates null value  #creating series   #in series all elements are of same type whereas in list multiple types
s.name='Practice'   #series can have name aslo
print(s)   #index and value printed
print(s.values)   #series is stored as numpy array
print(s.dtype)
print(s[4])   #index used similiarly as lists
print(s.index)   #to find pattern of idexes
s.index=['r','p','t','l','m','n','o','s','a','b']   #index can also be renamed (like dictionary)
#M2 pd.Series([6,76,....],index=[uyuyg.....]
#M3  pd.Series({'jh':756,'ug':7778})
#M4 pd.Series(s,index=['jh',....])
print(s)
print(s['r'])  #series are not random like dictionary
print(s.iloc[0])  #if after index name still want to find by index(location)
print(s[['t','m']])  #multiple indexes like numpy
print(s['p':'o'])   #slicing   #last index also included(different fom list )
#arithmetic operation are like numpy array
print(s*30)
#boolean also same as arrays
print(s[s>3])
#stats also same
print(s[(s>s.mean()) | (s<s.std())])
print(s[['p','o','s']].mean())   #o was none so not considered in no. of elements
#operator also same ~,|,&
#modifying list
s['o']=5
s[s>10]=0
print(s)
'''
#DataFrames   like excel  can be considered as combination of multiple series
a=pd.DataFrame(np.random.randint(1,500,(5,6)),index=['satyam','hj','jgf','jhf','jhft'],columns=['3r4','34f','3fr','3f3','34','fwe2'])  #index:row heading,columns=column heading   ,for any random number  random.randn(10,4)  10,4 size of array
'''
print(a)
#some basics
print(a.columns)
print(a.index)
print(a.info())    #information about DF
print(a.shape)
print(a.size)
print(a.dtypes)
print(a.describe())
print(a.dtypes.value_counts())   #count datatypes by columns as no. of columns of int type,float
print(a.to_numpy())  #convert to numpy
print(a.sort_index(axis=1,ascending=False))   #sort by column name
print(a.sort_index(axis=0,ascending=False))    #sort by index name
print(a.sort_values(by='3r4'))    #by a column value
'''
'''
d=pd.date_range('20200306',periods=10)   #array of dated (from YYYYMMDD to next 10)   using for indexing dataframes
print(d)
#creating dataframes from dictionary
dicdf=pd.DataFrame({'A':[1,np.NaN,np.nan,2],
                    'B':pd.Timestamp('20200306'),  #using fixed date
                    'C':pd.Series(1,index=list(range(4)),dtype='int32'),  #4 times 1
                    'D':np.array([5]*4,dtype='int32'),
                    'E':pd.Categorical(['True','False','True','False']),
                    'F':'satyam' })
print(dicdf.info())
print(dicdf)
#in this A,B,C,D will be column heading and their values be what is provided
print(dicdf.dtypes)  #dtype of all columns
print(dicdf.dtypes.value_counts())
'''
'''
#slicing
print(a.loc['satyam'])   #select by rows (row name(index))
print(a.iloc[-1])     #select by row by row index
print(a['3r4'])   #select column  also by index location
#colon can be used as in lists
#mixed
print(a.loc['satyam':'jhf','34f':'34'])   #here index location can't be used for that use iloc            if for multiple(using ,) put in list
'''
'''
#conditional boolean selection
print(a['3r4']>200)
print(a[a['3r4']>200])  #print rows in which value of '3r4' column >70  #for proper use a.loc outside
print(a.loc[a['3r4']>100,'3fr'])   #only print '3fr' column   #2nd dimension
'''
'''
#editting in dataframe
#dropping stuff
print(a.drop('satyam'))   #if permanently drop use a=a.drop   #multiple can also be dropped by comma and putting in list
print(a.drop(columns='3r4'))   #same as above
print(a['3r4']//10)
#a little bit confusing
print(a[['3r4','34f']]+pd.Series([-50,70],index=['3r4','34f']))  #-50 to all 3r4 column and +70 to 34f column
'''
'''
#modifying DataFrame
#create new column
t=pd.Series(['dc','ww'],index=['satyam','hj'])   #new column index name should be specified so that it can match with other   tose index not specified will have null value
a['added column']=t
#replacing per column
a['added column']='wde'   #all values of column would be changed to wde
#rename column and index names
print(a.rename(columns={'3r4':'C1','34f':'C2'},index={'hj':'I1'}))   #if column/index doesn't exist then no change   #change not permanent
#adding values  (index)
print(a.append(pd.Series({'3r4':'yfy','34f':'hjg'},name='did')))
#creating column using other column (for summation etc..)
a['summ']=a['3r4']+a['34f']   #permanent
print(a)
#mean,sum,max() can also be used   #column_name.sum()  to calculate horizontally
'''

#Reading files--csv,sml,html..
#reading csv
import matplotlib.pyplot as mpl
'''
cs=pd.read_csv('btc-market-price.csv',header=None)   #as no column heading so consider first line to be heading   to avoid use header
print(cs.head())                                     #here cs is a dataframe so all similiar function
cs.columns=['Timestamp','Price']
print(cs.head())   #as many rows so head() for 5 starting rows   use tail() for last 5
print(cs.tail(3))   #last 3
print(cs.dtypes)
cs['Timestamp']=pd.to_datetime(cs['Timestamp'])   #as dtype of timestamp is object, to convert in time
print(cs.head())
cs.set_index('Timestamp',inplace=True)   #making timestamp column as index column   #if inplace=True change will become permanent(return None) and using False inpace we have to write like cs=cs....  as change not permanent(return Dataframe)
print(cs.loc['2017-09-29'])   #as index column so we can find values directly
'''
'''
#doing all above with read csv in one line
cs=pd.read_csv('btc-market-price.csv',header=None,names=['Timestamp','Price'],index_col=0,parse_dates=True)   #names-column name,index col to assign 0th column as index,parse dates make index column date
print(cs.head())
#print(cs.plot())  #M1
print(mpl.plot(cs.index,cs['Price']))   #M2
mpl.show()  #to view graph, can be used in idle also
'''
'''
#plotting
x=np.arange(0,20)
a.plot()  #directly plot dataframe without matplotlib
mpl.plot(x,x**2)
mpl.plot(x,-1*x**2)
'''




