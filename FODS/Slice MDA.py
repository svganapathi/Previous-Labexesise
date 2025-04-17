import numpy as np
x = np.random.randint(10, size=(3, 4))
print('Array',x2)
print('Slice two rows and three columns')
print(x[:2,:3])
print('Slice three rows and two columns')
print(x[:3,::2])
print('Slice a particular value')
print(x[:1,:1])