## Carry Out Error Analysis

Error Analysis is the process of examining samples that the model predict incorrectly to find out the causes and solutions.

- Step 1: Get about 100 samples from dev set
- Step 2: Check each sample and categorize error into groups (e.g. big dog/cat bugs, blurry image error,...)
- Step 3: Counting the percentage of errors belonging in each group
- Step 4: Prioritize the error group which has the highest percentage to focus on improving

## Clean Up Incorrectly Labeled Data
**Example of incorrect label:** Suppose that we have the data of image with the label:
- `0` is dog
- `1` is cat

The data is like that:

|image|label|
|:-:|:-:|
|cat|1|
|dog|0|
|cat|1|
|cat|1|
|dog|0|
|**dog**|**1**|
|cat|1|

Here we can see that the $6^{th}$ observation is incorrectly labeled.

**So what should we do?**
- **For training set:** Deep Learning algorithms are quite robus with random errors in training set. If the error rate is not too high and the error is random, it can be left uncorrected. But if you want, you can still review and correct errors in the training set.

- **For dev sets and test sets**: If errors incorrectly labeled examples in **dev & test sets** significantly affect the ability ot evaluate algorithms on **dev set**, the it's worth taking the time to fix the bugs in **dev & test sets**.

- **How to fix**: During Error Analysis (EA), count 1 more column for incorrectly labeled examples. The calculate the percentage of errors due to incorrect labels. If the rate is significant, we should prioritize to correct them.

- **Principle**: Apply the same debugging process to both dev and test set. Check both true and false prediction examples. It may not be necessary to modify the training set if it is too large.