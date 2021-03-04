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
- **Pytorch Practice**
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
- **Pytorch Practice**
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
- **Theory of Deep Learning**
    - Basic Theory of **Word2Vec** 1
        - What is one-hot encoding 
        - CBOW
        - Skip-Gram
        - Why does it occur Imbalance overhead?
- **Pytorch Practice**
    -practicing Word2vec
        - Training Word2Vec through gensim  

>Assignment 
1) Crawling Instagram posting images based more than 5 hashtags 
2) confirm the result by calculating more than 10 word analogy
3) Try to score by putting more than 10 similarity pairs
    - ex) 'Benz' & 'BMW' 

## *Week 9* 
---
- **Data structure**
    - Stack
        - Concept of Stack 
        - How to use Stack functions in python 
            - ex)append(), pop() ..
    - Queue 
        - Concept of Queue
        - How to use Queue functions in python 
            - ex) append(), popleft(), appendleft(), pop() .. 
- **Theory of Deep Learngin**
    - Basic Theory of **Word2vec** 2 
        - About Distributional hypothesis 
        - Solutions for Imbalance overhead
            1) Hierarchical softmax
            2) Negative sampling 
        - Additional Performance Enhancement Techniques 
            - Subsampling 
- **Pytorch Practice**
    - Calculate Word analogy score by training several cases 

>Assignment 
1) Target 35% 
    - By increasing news dataset and iter, raise the score of word analogy task 
2) Coding Test about stack & queue on 'programmers'

## *Week 10*
---
- **Practice Algorithms** 
    - [practice 1](https://www.acmicpc.net/problem/11650)
    - [practice 2](https://www.acmicpc.net/problem/1463)
- **Theory of Deep Learning**
    - Basic Theory of RNN
        - About sequential data 
        - Concept of Recurrent Neural Network(RNN)
        - RNN applications 
            - Image Captioning
            - Sentiment classification 
            - Machine translation
            - Question answering
            - Language modeling 
        - Bidirectional RNN 
        - Limitation of RNN 
        - How to classify Text using RNN 
- **Pytorch Practice**
    - Movie review rating prediction using RNN model
>Assignment 
1) Target Accuracy 87% by adjusting hyper parameters of RNN 

## *Week 11*
---
- **Practice Algorithms**
    - [practice 1](https://programmers.co.kr/learn/courses/30/lessons/43238)
    - [practice 2](https://programmers.co.kr/learn/courses/30/lessons/43236)
- **Theory of Deep Learngin**
    - LSTM (Long Short Term Memory)
        - limitations of RNN 
        - concept of LSTM
            - Cell state?
            - Gate Mechanism
                - Forget gate layer
                - Output gate layer
                - Input gate layer
        - Update Old cell state to new cell state
- **Pytorch Practice**
    - Text classification using LSTM
        - Movie review rating prediction using LSTM
>Assignment 
1) Target Accuracy 88% by adjusting hyper parameters (feat. LSTM)

## *Week 12*
---
- **Practice Algorithms**
    - [practice 1](https://programmers.co.kr/learn/courses/30/lessons/42576)
    - [practice 2](https://programmers.co.kr/learn/courses/30/lessons/42578)
    - [practice 3](https://programmers.co.kr/learn/courses/30/lessons/42579)
- **Seq2Seq**
    - About Seq2Seq
    - Basic NMT (Neural Machine Translation)
        - Using methods in NMT 
            1) Beam Search
            2) Greedy Search 
- **Pytorch Practice**
    - Translation based LSTM 

## *Week 13*
--- 
- **Using Python**
    - Crawling of Youtube videos
        - Use Youtube class that is in Pytube 
- **Attention mechanism for NMT**
    - There are three types of Attention mechanism for NMT 
        1) Basic attention mechanism for NMT
        2) Multiplicative attention mechanism for NMT
        3) Additive attention mechanism for NMT 
    - Simple concept how to image captioning by Attention mechanism 
- **Pytorch Practice**
    - Attention mechanism NMT 

## *Week 14*
- **GAN (Generative Adversarial Network)**
    - About GAN 
        - Origin of the name ['Generative', 'Adversarial', 'Network']
        - About D(Discriminator) & G(Generator)
            1) Discriminator
                - Classification network classified as 0 or 1 based on data
            2) Generator
                - Distribution approximation function network that similarly expresses the distribution of training data
        - How to make G and D fight hostile?
        - Equation?
                - <img src="https://github.com/junginkim23/Deep_Learning_pytorch/blob/master/수식설명.PNG" width=300>
                - If Excellent D, Try to make the equation maximum(0)  
                - If Excellent G, Try to make the equation minimum(−∞)
        - There are several types of GAN
            1) Vanilla GAN
            - concept
                    - Use default MLP
            2) Conditional GAN
            - concept
                    - Insert The label that is the correct answer into D & G network together
                    - Label becomes a condition in the process of achieving its purpose! (both G & D)
            3) DCGAN
            - concept 
                    - Adjust CNN into GAN structure
                    - Generator uses Transpose Convolutional Network
                    - Discriminator uses Convolutional Network 
                    - It has guideline for stable Deep Convolutional GANs
                    - Operation can be performed using a random number(z)
            4) Conditional DCGAN
            - concept
                    - Conditioanl GAN + Deep Convolutional GAN
- **Pytorch Practice**
    - Train all types of GAN and then confirm the results.

## *Week 15*
- **About Action Recognition**

                    

        







