**Example of Sequence data**

![](img/1.png)

**Notation**

X: Harry Potter and Hermione Granger invented a new spell

y: 1 1 0 1 1 0 0 0 0

|Words|Value|
|:-:|:-:|
|Harry|1|
|Potter|1|
|and|0|
|Hermione|1|
|Granger|1|
|invented|0|
|a|0|
|new|0|
|spell|0

We denote that:

|..|..|
|:-:|:-:|
|$X^{(i)<t>}$|Training set|
|$T_X^{(i)}$|Length of $X^{(i)}$|
|$y^{(i)<t>}$|Output sequence|
|$T_y^{(i)}$|Length of $y^{(i)}$|

**Representing words**

Gated Recurrent Unit (GRU)

$c^{<t>} = \Gamma_u \times \tilde{c}^{<t>} + (1-\Gamma_u) \times c^{t-1}$