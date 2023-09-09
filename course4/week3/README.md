## Object Detection
> Learn how to apply your knowledge of CNNs to one of the toughest but hottest field of Computer Vision: **Object Detection**

### Object Localization
- Object detection is one of the areas in which Deep Learning is going great in the pass 2 years
- What are localization and detection?
    - Image classification
        > Classify an image to a specific class. The whole image represents 1 class. We don't want to know exactly where are the object. Usually only 1 object is presented.
        ![Alt text](Classification.jpg)

    - Classification with localization:
        > Given an image we want to learn the class of the image and where are the class location in the image. We need to detect a class and a rectangle of where that object is. Usually only 1 object is presented
        ![Alt text](ClassificationLoc.jpg)

    - Object Detection
        > Given an image we want to detect all the objects in the image that belong to a specific classes and give their location. An image can contain more than 1 object with different classes
        ![Alt text](ObjectDetection.png)

    - Segmantic Segmentation
        > - We want to label each pixel in the image with a category label. Segmantic Segmentation don't differentiate instances, only care about pixels. It detects no objects just pixels.
        > - If there are 2 objects of the same class is intersected, we won't be able to separate them.
        ![Alt text](SemanticSegmentation.png)

    - Instance Segmentation
        > This is like the full problem. Rather than we want to predict the bounding box, we want to know which pixel lable but alse distinguish them.
        ![Alt text](InstanceSegmentation.png)

- To make image classification we use a Convolutional Networks with a Softmax attached to the end of it

- To make classification with localization, we use a Convolutional Networks with a softmax attached to the end of it and 4 numbers: `bx`, `by`, `bh`, `bw` to tell you the location of the class in the image. The dataset should contain this 4 numbers with the class too.

- Example:

- Loss function:

### Landmark Detection

### Object Detection

### Convolutional Implement of Sliding Windows

### Bounding Box Predictions

### Intersection Over Union

### Non-max Suppression

### Anchor Boxes

### YOLO Algorithm