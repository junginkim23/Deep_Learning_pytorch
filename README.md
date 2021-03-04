# Deep Learning with pytorch

Foundations of diverse neural networks, AI SCHOOL course 

## *Week 1*
--- 
- **About AI** 
    - What is AI?
    - History of AI 
    - Examples of using AI 
- **About Python** 
    - Character of Python 
    - Data types of Python (Integer, float, character ...)
    - How to use List? 
    - String Formatting 
- **Basic Theory of Deep Learning** 
    - Process of Learning 
        1) Evaluation (Forward propagation)
            - softmax function 

        2) Loss and Gradient (Backpropagation)
            - Loss Function(Mean Squared Error & Cross Entropy error)
        3) Update (Optimize)
    - What is the perceptron? (and Multi-layer perceptron) 
- **Basic of Pytorch**

>**Assignment**
>1) Print some string using formatting 
>2) Sorting a list  


## *Week 2* 
---
- **About Python**
    - Dictionary? 
    - What is Function? & How to use Function? 
    - Control Statement
        - if
        - for 

- **Basic theory of Deep Learning**
    - Gradient decent & Learning rate 
    - Back propagation 
    - Optimizer 
        - SGD 
        - AdaGrad 
        - RMSProp
        - Momentum
        - Adam
- **Basic of Pytorch**
    - Developement of handwriting recognizer 
        - _it has a code._
    
>Assignment 
1) Making a Code
```py
num = 5 
if <num이 짝수라면>:
    print('짝수입니다.')
else: 
    print('홀수입니다.')
```
2) Calculation Back propagation 

## *Week 3*
---
- **About Python**
    - List nesting('for' Statement)
    - tuple
    - 'While' Statement
    - File I/O
- **'Deep Learning' Learning Methodology**
    - Early Stopping
    - Weight Initialization
    - Dropout
    - Parameter Norm Penalties 
    - Data Augmentation 
- **Development of handwriting recognizer with hyperparameter adjustment**
    - Epoch, Batch Size, Iterations 
    - Training, Test Set 
    - What is MNITST Dataset 
>Assignment
1) Using 'While' to make below problem
``` 
*
**
***
****
*****
```
2) Implement the below code in one line using list nesting.
```py
number = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 == 0:
        result.append(n+2)
```
3) Read the given fileIO.txt file, Key is Last Name and Value is
Allocate information to the dictionary name_age, which is the age, and then print it.

4) Set my own Hyper Pameter to to learn MNIST Dataset 

## *Week 4*
---
- **About Python**
    - Class 1
- **Theory of Deep Learning**
    - CNN(Convolution Neural Network)
- **Pythorch**
    - Classification of MNIST data using CNN model 

>Assignment
1) Create a Calculator class that performs four arithmetic operations

## *Week 5*
---
- **About Python**
    - Web crawling 
        - Using Beautiful Soap Package
        - Using IMDB Dataset 
- **Theory of Deep Learning**
    - Representative model using CNN
        - *_Just simple Theory_
        - LeNet
        - AlexNet
        - GoogleNet
        - ResNet
        
- **Pythorch**
    - Classification of CIFAR-10 data using LeNet
>Assignment 
1) Dynamic crawl of 100 dates and save date.txt (feat. IMDB Dataset)
2) Target 74 % by adjusting the hyperparameter(feat. LeNet)

## *Week 6*
--- 
- **About Python**
    - Class 2
        - Character of Class : Inheritance
- **Theory of Deep Learning**
    - Batch Normalization 
- **Pytorch**
    - Implement ResNet 18 
>Assignment 
1) Make ScienCalculator class that inherits Calculator class 
    - Add function - pow()_Calculate squared
    - Redefine 'class' by using method overriding 
    - Print the result by using 5 methods after creating ScienCalculator class 

2) Reimplement ResNet - 18 and then train the network using CIFAR 10 Dataset 
3) Implement ResNet - 101 

## *Week 7*
---
- **About Python**
    - Numpy
    - NLTK
    - pre-processing 
        - tokenize
        - Eliminate stopwords 
        - stemming  
- **Theory of Deep Learning**
    - CNN-based text classification
        - _김훈의 CNN_
- **Pytorch**
    - Movie review rating prediction using CNN model

>Assignment
1) Find the similarity between the 3 given sentences.
    - **step**
        - pre-processing
        - Implement Cosine similarity function
        - Make Doc-word matrix 
        - Finding the Similarity 
2) Target 90 % by adjusting Hyper parameter (CNN Classifier)

## *Week 8*
---
- **Using python**
    - Collect Instagram posts 
        - Hashtag-based image and text collection
- **Theory of Deep Learning 
    - Basic Theory of **Word2Vec**
        - What is one-hot encoding 
        - CBOW
        - Skip-Gram
- **Pytorch**
    -practicing Word2vec
        - Training Word2Vec through gensim  

>Assignment 
1) Crawling Instagram posting images based more than 5 hashtags 
2) confirm the result by calculating more than 10 word analogy
3) Try to score by putting more than 10 similarity pairs
    - ex) 'Benz' & 'BMW' 

## *Week 9* 
---