import numpy as np
a = np.array([1010, 1000, 998])
c = np.max(a)
e_a  = np.exp(a-c)
print(e_a)

s_e_a = np.sum(e_a)
print(s_e_a)
y=e_a/s_e_a
print(y)

#print((sum(y))
sy = np.sum(y)
print(sy)