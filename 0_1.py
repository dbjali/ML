1 + 1
1 - 2
3 * 5
7 / 5
2 ** 4

type(10)
type(2.14)
type("string")

x = 5
print(x)

x = 10
print(x)

y = 3.14
x * y

type(x * y)


a = [1,2,3,4,5]
print(a)
len(a)
a[0]
a[4]
a[4] = 99

print(a)

a[0:2]
a[1:]
a[:3]
a[:-1]
a[:-2]

d = {'height':180}
d['height']
d['weight']=70

print(d)

hungry=True
sleep=False

type(hungry)
not hungry

hungry = True
if hungry:
	print("I'm hungry")
hungry = False
if hungry:
	print("I'm hungry")
else:
	print("I'm not hungry")
	print("I'm sleepy")


def hello(obj):
	print("hello " + obj + "!")

hello("cat")




hungry.py
print("I'm hungry!")


man.py
# coding: utf-8
class Man:
    def __init__(self, name):
	self.name = name
	print("Initilized!")

    def hello(self):
	print("Hello " + self.name + "!")

    def goodbye(self):
	print("Good-bye " + self.name + "!")

m = Man("David")
m.hello()
m.goodbye()


import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x)

type(x)




x = np.array([1.0, 2.0, 3.0])

y = np.array([2.0, 4.0, 6.0])
x+y
x-y
x*y
x/y
x/2.0

a = np.array([[1,2], [3,4]])
print(a)
a.shape
a.dtype


b = np.array([[3,0], [0,6]])
a+b
a*b
print(a)
a*10


a = np.array([[1,2], [3,4]])
b = np.array([10,20])

a*b

x = np.array([[51,55],[14,19],[0,4]])
print(x)

x[0]
x[0][1]

for rw in x:
	print(rw)


x = x.flatten()
print(x)

x[np.array([0,2,4])]

x > 15
x[x > 15]


sin_graph.py
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

# 데이터 준비
x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1 간격으로 생성
y = np.sin(x)

# 그래프 그리기
plt.plot(x, y)
plt.show()



img_show.py
# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('../dataset/cactus.png') # 이미지 읽어오기

plt.imshow(img)
plt.show()



cos-sin_graph.py
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

# 데이터 준비
x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1 간격으로 생성
y1 = np.sin(x)
y2 = np.cos(x)

# 그래프 그리기
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle = "--", label="cos") # cos 함수는 점선으로 그리기
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름
plt.title('sin & cos')
plt.legend()
plt.show()