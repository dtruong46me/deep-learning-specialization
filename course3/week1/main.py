import numpy as np

x = np.random.randn(4,5)
y = np.sum(x, axis=1)

print(x)
print(y)
print(y.shape)