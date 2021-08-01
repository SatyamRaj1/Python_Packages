import numpy as np
a=np.array([[1,2,3],[4,5,6],[8,9,10]])  #two dimensional array each row separated by parenthesis
print('Array a',a)
b=np.array([[3,4,6],[1,3,2],[8,9,2]])
'''
#random
print(np.random.rand(4,2))  #arguement directly not tuple
print(np.random.random_sample(a.shape))  #shape from a
print(np.random.randint(3,10,size=(3,3)))   #random integers from 3 to 10(exclude) if only one no. then strting point 0
'''
'''
q=np.array([[[1,2,3],[4,5,6]],[[1,5,6],[4,6,8]]],dtype='int8')     #3d array having each element of size 1byte(1byte=8bit)
print(q.itemsize)
'''
'''  #to find memory occupied
s=range(100)  #defining list of elements from 0 to 99
import sys   #to find memory taken,...
print(sys.getsizeof(5)*len(s))    #getting size of any one element(here 5) and multiple witn length of string
d=np.arange(100)   #arange=array +range
print(d.size*d.itemsize)  #d.size give space occupied by one element of array d
'''
'''
#some types of matrix
print(np.zeros((2,4)))  #4 dimensional zero matrix with dimension 2,3,3,4  here 2 brackets
print(np.ones((2,4),dtype='int8'))
print(np.full((2,2),45)) #for any other numbers
print(np.full_like(a,6))  #take shape from already present array
print(np.full(a.shape,6))  #same as previous
print(np.identity(3))  #identity matrix
print(np.eye(3,3))  #diagonal matrix with each diagonal element 1
print(np.eye(4,8))   ##diagonal matrix
print(np.eye(4,8,k=1))   #diagonal matrix column shofted by 1
print(np.eye(4,8,k=-1))   #diagonal matrix row shifted by 1
'''
'''  #time
import time
size=100
l1=range(size)
l2=range(size)
a1=np.arange(size)
a2=np.arange(size)

start=time.time()
result=[x+y for x,y in zip(l1,l2)]  #zip is used to run loops in parallel
print((time.time()-start)*1000)   #time.time()  gives time taken by program till it is called

start=time.time()
result=a1+a2   #adding elements of array
print((time.time()-start)*1000)   #give is second so *1000 for milli
'''
'''
d=np.array([[1,2,3],[1,2,5],[2,4,6],[6,4,32]])
print(d)
print(d.ndim)  #to find dimension
print(d.itemsize) #to find bytes occupied by each element
print(d.size*d.itemsize)  #d.size give no. of elements and d.itemsize give bytes of one element  so it will be bytes by array
print(d.nbytes)  #to get size(bytes) of array directly
print(d.dtype)   #to print datatype of elements
print(d.size)   #total number of elements in array
print(d.shape)   #shape or dimensions

#reshaping (no. of rows and columns)
print(d.reshape(6,2))
print(d.ravel())   #to convert in only one row  M2 by reshape
''''''
#slicing
print(a[0,2])   #0th row and 2nd column  negative indexing can also be used
print(a[1:4,0:2])   #from 1st to 4th(not included) row and 0th to 2nd(not included)  column 
print(a[:,0:2])   #all rows and 0,1 column  can be written as a[0:,0:2]
a[1,:]=[1,2,3] #changing first row
a[1,:]=5  #changing whole row to value 5
print(a)
print(a[0,0:3:2])   #with jump of elements (like in for loop by 2 here)
print(a[0,1:-1])     #can also use +ve and -ve index in same
'''
'''b=[
#numbers lying b/w two numbers
b=np.linspace(1,4,20)   #store 20 equally spaced valued b/w 1 and 4(both included)
print(b)
'''

'''
#sum,max,min
print(a.max())
print(a.min())
print(a.sum())

#axis
print(a.sum(axis=0))  #axis0 means columns  so it will give sum of all columns(vertical)
print(a.sum(axis=1))  #axis1 means rows so it will give sum row wise
r=np.array([[1,2,3]])
print(np.repeat(r,3))  #repeat each element thrice
print(np.repeat(r,3,axis=0))  #repeat vertically
print(np.repeat(r,3,axis=1))   #repeat horizontally each element
'''
'''
#square root and standard deviation
print(np.sqrt(a))
print(np.std(a))   #to find standard deviation about any other no, then mean write ,b in brackect b=no.
'''
'''
#array addition,sub,multiplication
print(a,'\n')
print(b,'\n')
print(a+2,'\m','\n',a-2,'\n','\n',a*4,'\n','\n',a/2)  #add,sub,mult,divide each element can also power it
print(a+b,'\n','\n',a-b,'\n','\n',a*b,'\n','\n',a/b)
'''
'''
#concanate arrays
#vertical stack
print(np.vstack((a,b)))   #placing one on top of other (vertical)
#horizontal stack
print(np.hstack((a,b)))   #placing one ahead(to left) to other
#use double bracket only as other bracket make them a tuple(only one arguement in function)
'''
''';
###numpy special functions
import matplotlib.pyplot as pt  #to plot graph
#1 trigonometric function
x=np.arange(0,3*np.pi,0.1)   #no. b/w 0 and 3*pi and increment by 0.1 
y=np.sin(x)  #function from numpy
z=np.cos(x)
w=np.tan(x)
pt.ylabel('value')   #to name y axis
pt.xlabel('x')
pt.plot(x,y)
pt.plot(x,z)
pt.plot(x,w)
pt.show()   #for graphics
#2 exponential and logarithm(base=10) for natural log--ln
print(np.exp(a))   #e^all elements of a
print(np.log(a))   #natural log (base e) ln
print(np.log10(a))  #log base 10
'''
'''
#some miscallaneous
out=np.ones((7,7))
out[1:-1,1:-1]=np.zeros((5,5))
for i in range(2,4):
    out[i:-i,i:-i]=np.full((7-2*i,7-2*i),i)
print(out)
'''
'''
#linear algebra  matrix operations
m1=np.ones((3,2))
m2=np.full((2,3),2)
mul=np.matmul(m1,m2)   #matrix multiplication
print(mul)
print(np.linalg.det(mul))  #to find determinant
t=np.array([[1,2],[2,3]])
print(np.linalg.inv(t))  #inverse
a=np.array([1,2,3])
b=np.array([2,3,2])
print('dot',np.dot(a,b))  #dot product   also by a@b or a.dot(b)
print('cross',np.cross(a,b))    #cross product
print(a.T)    #transpose
'''
'''
#import file data from a file
filedata=np.genfromtxt('testfile.txt',delimiter=',')  #separate element into array by comma
print(filedata.astype('int32'))   #change each element datatype to int
print(filedata)  #by default float type
pq=np.array([2,4,5,2,4,2,5,2,5])
#boolean masking and advance indexing
print(filedata>50)  #to check each element
print(filedata[filedata>50])   #print values satisfying conditions
print(pq[[2,5,7]])   #numpy array can be indexed by list and here it will print 2,5,7th elements
print(np.any(filedata>20))  #or for all array (true if any in a array is >20
print(np.all(filedata>20)) #and for carray print true if all >20
print(np.all(filedata>20,axis=0))   #column wise
print(np.any(filedata>20,axis=1))   #row wise
print((filedata>20)&(filedata<100))   #multiple conditions
print(~((filedata>50)&(filedata<100)))  #here not symbol is different (~)
'''
'''      
#boolean selection
print(a[[True,False,True]])   #to print 0,2 element(here row)  true to select and false to deselect
print(a[a>2])  #a>2 gives boolean array which is used as previous
print(a[(a==1) | (a==6)])    #or operator
'''

