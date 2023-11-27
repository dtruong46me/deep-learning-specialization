
## Basic model

Ví dụ có 1 câu: 

`Jane visite I'Afrique en Septembre`

$\to$ `Jane is visiting Africa in September`

Sử dụng mã hóa x1, x2,...x5 $\to$ FR to EN: y1, y2,..y6


Ví dụ 2: **Image captioning**

Ví dụ có 1 bức ảnh, và output của nó là `A cat sitting on a chair`

Vậy làm cách nào để train (images) với output là captions???


Convolution -> AlexNet -> 4096-dimension Vector -> Sau đó đưa qua mạng RNN để generate


## Picking the most likely sentence

Ví dụ: Mahcine Translation

Language Model P(y1, y2,...yTy)

Khác với Language model (sử dụng probability cho từng output), MT sử dụng đầu vào là Encoding (nhưng LM chỉ sử dụng a0 cho đầu vào)

Machine Translation: Encoding and Decoding P(y1,y2,...yTy | x1,x2,...xTx)


**Finding the most likely translation**

Ví dụ: `Jane visite I'Afrique en Septembre`

$\to$ `Jane is visiting Africa in September`

$\to$ `Jane is going to visit Africa in September`

$\to$ `In September, Jane will visit Africa`

$\to$ `Her African friend welcomed Jane in September`

Do đó chúng ta phải chọn để maximize condition. Thuật toán sử dụng đó là Beam Search

**Tại sao không sử dụng Greedy Search?**

