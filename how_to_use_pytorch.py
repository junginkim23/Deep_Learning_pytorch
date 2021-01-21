# -*- coding: utf-8 -*-
"""How_to_use_pytorch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HJBI3Df_8Vq6OSqYwvng83ISxbeP88eo

## pytorch import
"""

import torch

"""## 0에서 1사이의 랜덤한 숫자"""

x = torch.rand(3, 4) #torch.rand(a,b) a-행, b-열
print(x)

"""## 정규분포에서 샘플링한 값 """

x = torch.randn(2, 3) 
print(x)

"""## 시작과 끝 사이의 랜덤한 자연수"""

x = torch.randint(2,6,size=(2,3)) #2~6 사이의 정수 중 랜덤하게 2행 3열에 맞춰 추출 
print(x)

"""## 0으로 채워진 텐서, 1으로 채워진 텐서 """

### 0으로 채워진 텐서
x = torch.zeros(2,3)
print(x)

ref = torch.rand(4,5)
x = torch.zeros_like(ref) #0~1사이의 랜덤한 숫자로 이루어진 4행 5열의 tensor를 인수로 받아, 행과 열의 size 마늠 0으로 채워준다.
print(x)

### 1로 채워진 텐서
x = torch.ones(2,3)
print(x)

### 인자로 들어오는 텐서와 형태가 같은 1로 채워진 텐서
ref = torch.rand(4, 5)
x = torch.ones_like(ref)
print(x)

import torch.nn as nn #nn->neural network? 
import numpy as np

x_data=np.array([[1.0,2.0]],dtype=np.float32)
#print(x_data.shape)
#print(type(x_data))
x_data=torch.from_numpy(x_data)
#print(x_data)
#x_data = torch.FloatTensor([1.0, 2.0])
#print(x_data)
torch.from_numpy
linear = nn.Linear(2, 1) #입력값과 가중치의 곱의 합이 이 코드에서 다 실행된다. 2개의 입력과 1개의 퍼셉트론 -> (2,1)
sigmoid = nn.Sigmoid()
# relu=nn.ReLU()

z=sigmoid(linear(x_data))
print(z)
# z = relu(linear(x_data))
# print(z)

print(linear.weight) #2개의 가중치를 확인할 수 있다.
print(linear.bias) #퍼셉트로은의 bias를 알 수 있다.

print(x_data)
print(x_data.shape)

linear(x_data)