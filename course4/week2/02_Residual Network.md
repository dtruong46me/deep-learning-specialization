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

### The Convolutional Block

![](img/convblock_kiank.png)

## Building ResNet Model (50 layers)

![](img/resnet_kiank.png)
<p style="text-align: center">Figure 5: ResNet-50 model</p>
