import numpy as np

class ConvolutionalNeuralNetwork:
    def __init__(self, X: np.ndarray) -> None:
        self.X = X

    def zero_pad(self, pad: int) -> np.array:
        X_pad = np.pad(self.X, ((0,0), (pad,pad), (pad,pad), (0,0)), 'constant', constant_values=0)

        return X_pad
    
    def conv_single_step(self, a_slice_prev, W, b):
        s = np.multiply(a_slice_prev, W)
        Z = np.sum(s)
        Z = np.float64(Z+b)

        return Z
    
    def conv_forward(self, A_prev, W, b, hparameters):

        cache = (A_prev, W, b, hparameters)

        return cache
    
    def pool_forward(self, A_prev:np.ndarray, hparameters, mode="max"):
        (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape

        f = hparameters["f"]
        stride = hparameters["stride"]

        n_H = int(1+n_H_prev - f) / stride
        n_W = int(1+n_W_prev - f) / stride
        n_C = n_C_prev

        A = np.zeros((m, n_H, n_W, n_C))

        cache = (A_prev, hparameters)

        return A, cache
    
    def conv_backward(self, dZ, cache):

        return
    
    def create_mask_from_window(self):
        
        return
    
    def distribute_value(self, dz, shape):
        
        return
    
    def pool_backward(self, dA, cache, mode="max"):
        return