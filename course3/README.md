## Machine Learning Strategy 1
### Why Machine Learning Strategy
**Ideas for improving the accuracy of Deep Learning System**
- Collect more data
- Collect more diverse training set
- Train Algorithm longer with gradient descent
- Try different Optimization Algorithms (e.g. Adam)
- Try bigger network
- Try smaller network
- Try dropout
- Add L2 regularization
- Change Network Architecture (Activation Function, Hidden Networks,...)

### Orthogonalization

### Single Number Evaluation Metric
- It's better and faster to set a single number evaluation metric for your project before you start it
- Difference between precision and recall
    - Suppose we run the classifier on 10 images which are 5 cats and 5 non-cats. The classifier identifies that there are 4 cats, but it identified 1 wrong cat
    - Confusion matrix:

    ||Predicted Cat|Predicted Non-Cat|
    |-|:-:|:-:|
    |Actual Cat|3|2|
    |Actual Non-Cat|1|4|

    - Precision: Percentage of true cats in the recognized result: $precision=\frac{3}{3+1}$
    - Recall: Percentage of true recognition cat of the all cat prediction: $recall=\frac{3}{3+2}$
    - Accuracy: $\frac{(3+4)}{10}$

- Using a precision/recall for evaluation is a good in a lot of cases, but separately they don't tell you which algorithms is better.
- A better thing is to combine precision and recall in one single (real) number evaluation metric. There a metric call `F1` score, which combines them: $f1=2\times(\frac{1}{precision} + \frac{1}{recall})$

### Satisfying & Optimizing Metric

### Train/Dev/Test Distributions
- Dev and test sets have to come from the same distribution.
- Choose dev set and test set to reflect data you expect to get in the future and consider important to do well on.
- Setting up the dev set, as well as the validation metric is really defining what target you want to aim at.

**Size of the dev and test sets**
- An old way of splitting the data was 70% training, 30% test or 60% training, 20% dev, 20% test.
- The old way was valid for a number of examples ~ <100000
- In the modern deep learning if you have a million or more examples a reasonable split would be 98% training, 1% dev, 1% test.

### When to Change Dev/Test set & Metrics

|Metric|Classification Error|
|-|-|
|Algorithm A|3% error (But a lot of porn images are treated as cat images here)|
|Algorithm B|5% error|

### Why Human-Level Performance

### Avoidable Bias

### Understanding Human-Level Performance

### Suppass Human-Lever Performance

### Improve Model Performance

## Machine Learning Strategy 2
### Carrying out Error Analysis

### Cleaning up Incorrectly Labeled Data

### Build your first System Quickly, then iterate

### Training & Testing on Different Distribution

### Bias and Variance with Mismached data Distribution

### Addressing data mismatch

### Transfer Learning

### Multi-task Learning

### What is End-to-end Deep Learning

### Whether to use End-to-end Deep Learning


## Machine Learning Strategy 2

### Carry out Error Analysis

- Sometimes you can evaluate multiple Error Analysis ideas in parallel and choose the best idea. Create a spreadsheet to do that and decide, e.g.

    |Image|Dog|Great Cats|Blurry|Instagram Filter|Comments|
    |:-:|:-:|:-:|:-:|:-:|:-:|
    |1|&check;|||&check;|Pitbull|
    |2|&check;||&check;|&check;||
    |3|||||Reiny day at zoo|
    |4||&check;||||
    |...|
    |**%total**|**8%**|**43%**|**61%**|**12%**|

    > In the last example you will decide to work on **Great Cat** or **Blurry** images to improve your performance

[![Anurag's GitHub stats](https://GitHub-readme-stats.vercel.app/api?username=dtruong46me)](https://GitHub.com/dtruong46me/deep-learning-specialization) 