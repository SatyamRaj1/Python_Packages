import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
#to view in idle use pt.show()

x=np.arange(-10,11)

#Global API
pt.figure(figsize=(12,6))
pt.title('GRAPH')
pt.subplot(1,2,1)  #rows,columns, quadrant number
pt.plot(x,x**2)
pt.plot([-10,0,10],[-10,0,100])
pt.legend(['x^2','Vertical Line'])
pt.xlabel('X') #x axis name
pt.ylabel('X square')  #y axis name
pt.subplot(1,2,2)  #rows,columns, quadrant number
pt.plot(x,x**2)
pt.plot([-10,0,10],[-10,0,100])
pt.legend(['x^2','Horizontal Line'])
pt.xlabel('X') #x axis name
pt.ylabel('X square')  #y axis name

#OOP Interface
#if a report is long than we have to look what is happening top down in above method
fig,axes=pt.subplots(figsize=(12,6))
axes.plot(
    x,(x**2),color='red',linewidth=3,
    marker='o',markersize=8,label='x^2')
axes.plot(
    x,-1*(x**2),'b--',label='-x^2')
a=np.random.rand(50)
b=np.random.rand(50)
col=np.random.rand(50)
area=np.pi*(20*np.random.rand(50))**2
pt.figure(figsize=(14,6))
pt.scatter(a,b,s=area,c=col,alpha=0.5,cmap='Spectral')  #s for size, c for color so 4 dimension
pt.scatter(x,x**2)   #only points not line

