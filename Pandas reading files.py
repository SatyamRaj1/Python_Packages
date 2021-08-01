#csv--comma separated value --store in tabular form
import numpy as np
import pandas as pd
'''
with open('btc-market-price.csv','r') as fp:
    print(fp)
    for index,line in enumerate(fp.readlines()):
        #read first 10 lines
        if (index<10):
            print(index,line)
            timestamp,price=line.split(',')
            print(f"{timestamp}:${price}")
    
'''
#reading with pandas   #more understandable
#pd.read_csv?  #to know parameters  #only in online compiler or notebook
'''csv_url="https://raw.githubusercontent.com/ine-rmotr-curriculum/RDP-Reading-Data-with-Python-and-Pandas/master/unit-1-reading-data-with-python-and-pandas/lesson-1-reading-csv-and-txt-files/files/exam_review.csv"
#reading file from link
print(pd.read_csv(csv_url).head())
'''
'''
bt=pd.read_csv('btc-market-price.csv',
         header=None)
print(bt.head())
#converting missing values to null values
ab=pd.read_csv('btc-market-price.csv',
               header=None,
               na_values=['','?','-'],   #all empty, ?, - get converted to nan
               names=['time','price'],
               dtype={'price':'float'})
print(ab.head())
print(ab.dtypes)
print(pd.to_datetime(ab['time']).head())
ab['time']=pd.to_datetime(ab['time'])
print(ab.head())   #typecasting
ex=pd.read_csv('exam_review.csv')
print(ex)
ex=pd.read_csv('exam_review.csv',sep='>')   #sep just as delimator , separate on basis of given symbol
print(ex)
#excluding specific lines
ex=pd.read_csv('exam_review.csv',sep='>',skiprows=[1,3],decimal=',',skip_blank_lines=True)
print(ex)
#saving
ex
ex.to_csv('out.csv')  #another file with this name
'''

