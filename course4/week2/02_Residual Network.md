## The Problem of Very Deep Neural Networks

![](img/vanishing_grad_kiank.png)

<p style="text-align: center">Figure 1: Vanish Gradient</br>The speed of learning decrease very rapidly for the shallower layers as the network trains</p>

## Building a Residual Network

![](img/skip_connection_kiank.png)

<p style="text-align: center">Figure 2: A ResNet block showing a Skip-Connection</p>

### The Identity Block

![](img/idblock2_kiank.png)
<p style="text-align: center">Figure 3: Identity block. Skip connection "skips over" 2 layers</p>

![](img/idblock3_kiank.png)
<p style="text-align: center">Figure 4: Identity block. Skip connection "skips over" 3 layers</p>

```
def identity_block(X, f, initializer=random_uniform):
    F1, F2, F3 = filters
    X_shortcut = X

    X = Conv2D(filters=F1, kernel_size=1, strides=(1, 1), padding='valid', kernel_initializer=initializer(seed=0))(X)
    X = BatchNormalization(axis=3)(X)
    X = Activation('relu')(X)

    X = Conv2D(filters=F2, kernel_size=f, strides=(1, 1), padding='same', kernel_initializer=initializer(seed=0))(X)
    X = BatchNormalization(axis=3)(X)
    X = Activation('relu')(X)

    X = Conv2D(filters=F3, kernel_size=1, strides=(1,1), padding='valid', kernel_initializer=initializer(seed=0))(X)
    X = BatchNormalization(axis=3)(X)

    X = Add()([X, X_shortcut])
    X = Activation('relu')(X)

    return X
```

Where:
- X: Input tensor of shape($m, n_{H_{prev}}, n_{W_{prev}}, n_{C_{prev}} $)
- f: Integer, specifying the shape of the middle CONV's window for the main path
- filters: List of integers
- initializer: to set up the initial weights of a layer

- $\to$ X: output of the identity block, tensor of shape($m, n_H, n_W, n_C $)

### The Convolutional Block

![](img/convblock_kiank.png)

