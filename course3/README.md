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

### Clean up incorrect labeled data
- If you want to check for mislabeled data in dev/test set, you should also try error analysis with the mislabeled column. Ex:
    |Image|Dog|Great Cats|Blurry|Instagram Filter|Comments|
    |:-:|:-:|:-:|:-:|:-:|:-:|
    |1|&check;|||&check;|Pitbull|
    |2|&check;||&check;|&check;||
    |3|||||Reiny day at zoo|
    |4||&check;||||
    |...|
    |**%total**|**8%**|**43%**|**61%**|**12%**|

    > Then:
    > - If overall dev set error: 10%
    >   - Then Errors due to incorrect data: 0.6%
    >   - Then Error due to other causes: 9.4%
    > - Then you should focus on the 9.4 error rather than the incorrect data

- Consider these guidelines while correcting the dev/test mislabeled examples:
    - Apply the same process to your dev and test sets to make sure they continue to come from the same distribution
    - Consider examining examples your algorithm got right as well as ones it got wrong. (Not always done if you reached a good accuracy)
    - Train and (dev/test) data may now come from a slightly different distributions.
    - It's very important to have dev and test sets to come from the same distribution. But it could be OK for a train set to come from slightly other distribution.

### Build your first system quickly, then itarate

### Training and testing on different distributions

### Training and Testing on different distribution

### Bias and Variance with mismatch data distributions
- Bias and Variance analysis changes when training and Dev/Test set is from the different distribution
- Example: The cat classification example. Suppose you worked in the example and reached this:
    - Human Error: 0%
    - Train Error: 1%
    - Dev Error: 10%

    > In this example, you will think that this is a **variance problem**, but because the distributions are not the same, you can tell for sure. Because it could be that train set was easy to train on, but the dev set was more difficult

- To solve this issue, we create a new set called train-dev set as a random subset of the training set (so it has the same distribution) and we get: 
    - Human error: 0%
    - Train error: 1%
    - Train-dev error: 9%
    - Dev error: 10%
    > Now we are sure that this is a high variance problem

- Suppose we have a different situation:
    - Human error: 0%
    - Train error: 1%
    - Train-dev error: 1.5%
    - Dev error: 10%
    > In this case, we have something called **Data mismatch** problem

- Conclustion
    - Human-level error (proxy for Bayes error)
    - Train error:
        - Calculate `avoidable bias = training error - human error`

        > If the difference is big, then its **Avoidable bias** problem then you should use a strategy for high bias
    - Train-dev error
        - Calculate `variance = train-dev error - training-error`

        > If the difference is big, then its **High variance** problem, then you should use a strategy for solving it

    - Dev error
        - Calculate `data mismatch = dev error - train-dev error`

        > If difference is much bigger, then train-dev erorr is **Data mismatch** problem

    - Test error
        - Calculate `degree of overfitting to dev set = test error - dev error`
        
        > Is the difference is big (positive) then maybe you need to find a bigger dev set (dev set and test set come from the same distribution, so the only way for there to be a huge gap here, for it to do much better on the dev set than the test set, is if you somehow managed to overfit the dev set).

- Unfortunately, there aren't many systematic ways to deal with data mismatch. There are some things to try about this in the next section.

### Addressing data mismatch

### Transfer Learning

### Multi-task Learning

### What is End-to-end Deep Learning