import numpy as np

def sigmoid(z:np.array):
    sigmoid = 1 / (1 + np.exp(-z))

    return sigmoid

def initialize_with_zeros(dim:int):
    w = np.zeros((dim, 1))
    b = 0.0

    return w,b

if __name__ == '__main__':
    x = np.array([0.5, 0, 2.0])
    output = sigmoid(x)

    print(type(x))
    print(x)
    print(output)
    print(type(output))