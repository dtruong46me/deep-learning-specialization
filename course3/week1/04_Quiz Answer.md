
## Bird Recognition in the City of Peacetopia 

### Question 1 
**Problem Statement**

This example is adapted from a real production application, but with details disguised to protect confidentiality.

You are a famous researcher in the City of Peacetopia. The people of Peacetopia have a common characteristic: they are afraid of birds. To save them, you have **to build an algorithm that will detect any bird flying over Peacetopia** and alert the population.

The City Council gives you a dataset of 10,000,000 images of the sky above Peacetopia, taken from the city’s security cameras. They are labeled:

- y = 0: There is no bird on the image
- y = 1: There is a bird on the image

Your goal is to build an algorithm able to classify new images taken by security cameras from Peacetopia.

There are a lot of decisions to make:
- What is the evaluation metric?
- How do you structure your data into train/dev/test sets?

**Metric of success**

The City Council tells you that they want an algorithm that
1. Has high accuracy.
2. Runs quickly and takes only a short time to classify a new image. 
3. Can fit in a small amount of memory, so that it can run in a small processor that the city will attach to many different security cameras.

**Note:** Having three evaluation metrics makes it harder for you to quickly choose between two different algorithms, and will slow down the speed with which your team can iterate. True/False?
- [x] True
- [ ] False

---
### Question 2
After further discussions, the city narrows down its criteria to: 
- "We need an algorithm that can let us know a bird is flying over Peacetopia as accurately as possible."
- "We want the trained model to take no more than 10 sec to classify a new image.” 
- “We want the model to fit in 10MB of memory.” 

If you had the three following models, which one would you choose?

- [ ]

|Test Accuracy| Runtime| Memory size|
|:-:|:-:|:-:|
|99%|13sec|9MB|

- [ ]

|Test Accuracy| Runtime| Memory size|
|:-:|:-:|:-:|
|97%|1sec|3MB|

- [ ]

|Test Accuracy| Runtime| Memory size|
|:-:|:-:|:-:|
|97%|3sec|2MB|

- [x]

|Test Accuracy| Runtime| Memory size|
|:-:|:-:|:-:|
|98%|9sec|9MB|

This model has the highest test accuracy, the prominent criteria you are looking for, compared with other models, and also has a runtime <10 seconds and memory size < 10MB.

---
### Question 3
Which of the following best answers why it is important to identify optimizing and satisficing metrics?

- [x] Identifying the metric types sets thresholds for statisficing metrics. This provides explicit evaluation criteria
- [ ] Identifying the optimizing metric informs the team which models they should try first
- [ ] Knowing the metrics provides input for efficient project planning
- [ ] It isn't. All metrics must me met for the model to be

---
### Question 4
With 10,000,000 data points, what is the best option for train/dev/test splits?
- [x] train - 95%, dev - 2.5%, test - 2.5%
- [ ] train - 33.3%, dev - 33.3%, test - 33.3%
- [ ] train - 60%, dev - 30%, test - 10%
- [ ] train - 60%, dev - 10%, test - 30%

---
### Question 5
After setting up your train/dev/test sets, the City Council comes across another 1,000,000 images, called the “citizens’ data”. Apparently the citizens of Peacetopia are so scared of birds that they volunteered to take pictures of the sky and label them, thus contributing these additional 1,000,000 images. These images are different from the distribution of images the City Council had originally given you, but you think it could help your algorithm. 

Notice that adding this additional data to the training set will make the distribution of the training set different from the distributions of the dev and test sets.

Is the following statement true or false?

"You should not add the citizens' data to the training set, because if the training distribution is different from the dev and test sets, then this will not allow the model to perform well on the test set."

- [ ] True
- [x] False

Sometimes we'll need to train the model on the data that is available, and its distribution may not be the same as the data that will occur in production. Also, adding training data that differs from the dev set may still help the model improve performance on the dev set. What matters is that the dev and test set have the same distribution.

---
### Question 6
One member of the City Council knows a little about machine learning, and thinks you should add the 1,000,000 citizens’ data images to the test set. You object because:

- [x] The test set no longer reflects the distribution of data (security cameras) you most care about
- [ ] The 1,000,000 citizens data images do not have a consistent x $\to$ y mapping as the rest of the data
- [ ] A bigger test set will slow down the speed of iterating because of the computational expense of evaluating models on the test set
- [x] This would because the dev and test set distributions to become different. This is a bad idea because you're not aiming where you want to hit

---
### Question 7
You train a system, and the train/dev set errors are 3.5% and 4.0% respectively. You decide to try regularization to close the train/dev accuracy gap. Do you agree?

- [x] No, because you do not know what the human performance level is
- [ ] Yes, because having a 4.0% training error shows you have a high bias
- [ ] Yes, because this shows your bias is higher than your variance
- [ ] No, because this shows your variance is higher than your bias

You need to know what the human performance level is to estimate avoidable bias.

---
### Question 8
You ask a few people to label the dataset so as to find out what is human-level performance. You find the following levels of accuracy:
|-|Error|
|-|:-:|
|Bird watching expert #1|0.3% error|
|Bird watching expert #2|0.5% error|
|Normal person #1 (not a bird watching expert)|1.0% error|
|Normal person #2 (not a bird watching expert)|1.2% error|

If your goal is to have “human-level performance” be a proxy (or estimate) for Bayes error, how would you define “human-level performance”?

- [ ] 0.0% (because it is impossible to do beter than this)
- [ ] 0.75% (average of all 4 numbers above)
- [x] 0.3% (accuracy of expert #1)
- [ ] 0.4% (average of 0.3 and 0.5)

---
### Question 9
Which of the below shows the optimal order of accuracy from worst to best?

- [x] Human-level performance $\to$ the learning algorithm's performance $\to$ Bayes error
- [ ] Human-level performance $\to$ Bayes error $\to$ the learning algorithm's performance 
- [ ] The learning algorithm's performance $\to$ Bayes error $\to$ human-level performance 
- [ ] The learning algorithm's performance $\to$ human-level performance $\to$  Bayes error

No. HLP may be better than your algorithm's performance but it cannot be better than BE.

---
### Question 10
Which of the following best expresses how to evaluate the next steps in your project when your results for human-level performance, train, and dev set error are 0.1%, 2.0%, and 2.1% respectively?

- [ ] Keep tuning until the train set accuracy is equal to human-level performance because it is the optimizing metric
- [ ] Port the code of the target devices to evaluate if your model meets or exceeds the satisficing metrics
- [ ] Evaluate the test set to determine the magnitude of the variance
- [ ] Based on differences between the three levels of performance, prioritize actions to decrease bias and iterate

No. Always choose the area with the biggest opportunity for improvement.

**Question 10**


---
### Question 11
After running your model with the test set you find it is a 7.0% error compared to a 2.1% error for the dev set and 2.0% for the training set. What can you conclude? (Choose all that apply)

- [ ] Try decresing regularization for better generalization with the dev set
- [x] You should try to get a bigger dev set
- [x] You have overfitted to the dev set
- [ ] You have underfitted to the dev set

---
### Question 12
After working on this project for a year, you finally achieve: Human-level performance, 0.10%, Training set error, 0.05%, Dev set error, 0.05%. Which of the following are likely? (Check all that apply.)

- [ ] This result is not possible since it should not be possible to suppas human-level performance
- [x] Pushing to even higher accuracy will be slow because you will not be able to easily identify sources of bias
- [ ] There is still avoidable bias
- [x] The model has recognized emergent features that humans cannot (Chess and Go for example)
- [x] All or almost all of the avoidable bias has been accounted for
- [ ] This is a statistical anomaly (or must be the result of statistical noise) since it should not be possible to surpass human-level performance
- [ ] With only 0.05% further progress to make, you should quickly able to close the remaining gap to 0%
- [x] You are close to Bayes error and possible overfitting

---
### Question 13
It turns out Peacetopia has hired one of your competitors to build a system as well. You and your competitor both deliver systems with about the same running time and memory size. However, your system has higher accuracy! Still, when Peacetopia tries out both systems, they conclude they like your competitor’s system better because, even though you have higher overall accuracy, you have more false negatives (failing to raise an alarm when a bird is in the air). What should you do?

- [ ] Apply regularization to minimize the false negative rate
- [ ] Pick false negative rate as the new metric, and use this new metric to drive all further development
- [ ] Ask your team to take into account both accuracy and false negative rate during development
- [x] Brainstorm with your team to refine the optimizing metric to include false negatives as they further develop the model

Yes. The target has shifted so an updated metric is required.

---
### Question 14
You’ve handily beaten your competitor, and your system is now deployed in Peacetopia and is protecting the citizens from birds! But over the last few months, a new species of bird has been slowly migrating into the area, so the performance of your system slowly degrades because your model is being tested on a new type of data. There are only 1,000 images of the new species. The city expects a better system from you within the next 3 months. Which of these should you do first?

- [x] Add the new images and split them among train/dev/test
- [ ] Put them into the dev set to evaluate the bias and re-tune
- [ ] Augument your data to increase the images of the new bird
- [ ] Add hidden layers to further refine feature development

No. The number of new images is too small to make a difference.

---
### Question 15
The City Council thinks that having more Cats in the city would help scare off birds. They are so happy with your work on the Bird detector that they also hire you to build a Cat detector. You have a huge dataset of 100,000,000 cat images. Training on this data takes about two weeks. Which of the statements do you agree with? (Check all that agree.)

- [x] Lowering the number of images will reduce training time and likely allow for an acceptable trade-off between iteration speed and accuracy
- [x] This significantly impacts iteration speed
- [ ] Reducing the model complexity will allow the use of the larger dataset but preserve accuracy
