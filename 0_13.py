import numpy as np
x=np.array([1,2,3])
x.__class__

x.shape

x.ndim

w=np.array([[1,2,3],[4,5,6]])
w.shape
w.ndim

x=np.array([[1,2,3],[4,5,6]])
w=np.array([[0,1,2],[3,4,5]])
w+x
w*x

a=np.array([[1,2],[3,4]])
a*10

a=np.array([[1,2],[3,4]])
b=np.array([10,20])
a*b

a=np.array([1,2,3])
b=np.array([4,5,6])

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])

a=np.arange(2*3*4).reshape((2,3,4))
b1=np.arange(2*3*4).reshape((2,3,4))
b2=np.arange(2*3*4).reshape((2,4,3))
b3=np.arange(2*3*4).reshape((3,2,4))
b4=np.arange(2*3*4).reshape((3,4,2))
b5=np.arange(2*3*4).reshape((4,2,3))
b6=np.arange(2*3*4).reshape((4,3,2))
