## Single Number Evaluation Metric

Example

| Algorithm | US | China | India | Other | Average |
| :-: | :-: | :-: | :-: | :-: | :-: |
| A | 3% | 7% | 5% | 9% | 6% |
| B | 5% | 6% | 5% | 10% | 6.5% |
| C | 2% | 3% | 4% | 5% | 3.5% |
| D | 5% | 8% | 7% | 2% | 5.25% |
| E | 4% | 5% | 2% | 4% | 3.75% |
| F | 7% | 11% | 8% | 12% | 9.5% |

## Satisficing and Optimizing Metric

Another cat classification example

|Classifier|Accuracy|Runtime|
|:-:|:-:|:-:|
|A|90%|80ms|
|**B**|**92%**|**95ms**|
|C|95%|1500ms|

$cost = accuracy - 0.5 \times runtime$

$\to$ maximize accuracy subject to runtime $\leq$ 100ms

## Train/Dev/Test Distributions
Regions:
- US
- UK
- Other Europe
- South America
- India
- China
- Other Asia
- Australia

$\to$ Randomly shuffle into dev/test

## Size of the Dev and Test Sets
**Old way of splitting data**: 
- Train: 70%, Test: 30%
- Train: 60%, Dev: 20%, Test: 20%
- Train: 98%, Dev: 1%, Test: 1%

The traditional rule of thumb for splitting data into train, dev, and test sets is 70/20/10. However, this rule of thumb may not be appropriate for large data sets.

In the era of big data, it is more common to use a 98/1/1 split, with 98% of the data in the training set, 1% in the dev set, and 1% in the test set.

The dev set is used to evaluate different ideas and hyperparameters, while the test set is used to evaluate the final model.

The size of the dev set should be large enough to be statistically significant, but it should not be so large that it becomes too similar to the training set.

The size of the test set should be large enough to give a reliable estimate of the model's performance on unseen data.

Here are the problems with the 70/20/10 and 60/20/20 splits:
- These splits may not be large enough to be statistically significant, especially for small data sets.
- These splits may not be large enough to evaluate different ideas andhyperparameters.
- The test set may be too small to give a reliable estimate of the model's performance on unseen data.

Use a 98/1/1 split for large data sets to ensure that there is enough data for training, while still leaving enough data for evaluating different ideas andhyperparameters and for getting a reliable estimate of the model's performance on unseen data.

**Size of Test Set**

Set your Test Set to be big enough to give high conficence in the overall performance of your system

Make sure that the train, dev, and test sets are drawn from the same distribution. This means that the data in each set should have the same statistical properties.

Shuffle the data before splitting it into train, dev, and test sets. This will help to ensure that the data in each set is representative of the overall data set.

Use a random number generator to split the data. This will help to ensure that the split is truly random.

## When to Change Dev/Test Sets and Metrics?

- Your evaluation metric and dev/test sets act like a target for your team to aim at. Sometimes you may realize you've put the target in the wrong place and need to move it.

- If your metric is not properly ranking which algorithm is better, it's a sign you should change the metric or dev/test sets. 

- An example is a cat classifier metric using error rate, but one algorithm lets through porn images. So you should change the metric to heavily penalize misclassifying porn.

- Think of defining the metric and doing well on it as separate steps. First get the target right, then figure out how to aim at it.

- If your metric and dev/test sets don't reflect real user data, change them so they better match what matters for your app's performance. 

- Having a metric and dev/test sets, even imperfect ones, allows faster iteration. But don't keep a bad metric too long - change it when you have a better sense of what matters.

- The key is having a well-defined target to efficiently aim at, even if you need to adjust it later when you learn more.