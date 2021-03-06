# -*- coding: utf-8 -*-
"""Applying a lot of data to word2vec

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d3zBXt8_H3n2yQb7hs98VTLXDg7d5vv5
"""

# 나의 Drive를 연결하고 파일의 위치를 정확히 입력해야 함
# 띄어쓰기의 경우는 띄어쓰기 앞에 역슬래쉬(\) 기호를 넣고 띄어줘야 함 
# cp : copy 명령어 
# cp A B : A를 복사해서 B의 위치에 붙여 넣어라 

!cp drive/MyDrive/AI\ School/8주차/GoogleNews-vectors-negative300.bin.gz .
!cp drive/MyDrive/AI\ School/8주차/news1.txt .
!gunzip -k GoogleNews-vectors-negative300.bin.gz

!cp drive/MyDrive/AI\ School/9주차/questions-words.txt .

from google.colab import drive
drive.mount('/content/drive')

from gensim.test.utils import get_tmpfile
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence, PathLineSentences
from gensim.models.keyedvectors import KeyedVectors

"""# 1. News1.txt 데이터 이용 word2vec 학습"""

# news1.txt 학습 및 word analogy 평가 

sentences = LineSentence("news1.txt") 
model = Word2Vec(sentences, size=100, window=5, min_count=1, workers=4) #이게 학습 코드
model.save("word2vec_news1.model") #모델 save

model = Word2Vec.load("word2vec_news1.model")
score, predictions = model.wv.evaluate_word_analogies('questions-words.txt') #wv-word_vector 
print(score)

print(predictions)

"""# 2. Hyper parameter 변경 word2vec 학습"""

# hyper parameter 변경 학습 및 word analogy 평가 

sentences = LineSentence("news1.txt")
model = Word2Vec(sentences, size=300, window=10, min_count=5, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.0001, iter=10)
model.save("word2vec_hyper.model")

model = Word2Vec.load("word2vec_hyper.model")
score, predictions = model.wv.evaluate_word_analogies('questions-words.txt')
print(score)

print(predictions)

"""# 3. Google pre-trained word2vec 모델 사용"""

# Google의 pre-trained 모델 사용 word analogy 평가 
model = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True , limit=60000)
score, predictions = model.evaluate_word_analogies('questions-words.txt')
print(score)

"""# 4. One billion new dataset(중 일부) 사용 word2vec 학습"""

# zip 파일 풀고 1billion 폴더 안에 넣기 
!mkdir 1billion #디렉토리 생성 
!unzip drive/MyDrive/AI\ School/9주차/1-billion-part.zip -d 1billion/ #생성한 디렉토리에 집파일 생성 
!rm -r 1billion/__MACOSX/ #기존의 집업 파일에 있는 백업 파일을 삭제해라, -r이라는 것은 폴더를 지울 때 넣는 옵션.

import time

# One billion news dataset(중 일부) 사용 word2vec 학습

sentences = PathLineSentences("./1billion/") #PathLineSentences함수는 폴더를 입력으로 받아서, 폴더 안에 각각의 파일들안에 라인들을 읽어온다.

s=time.time()

model = Word2Vec(sentences, size=800, window=40, min_count=25, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.001, iter=4)
model.save("word2vec_1billion.model")

print((time.time()-s)/60)

(0.9126198536819882 *3600) /60

print(model.wv.vocab) #vocab에 대한 정보가 나온다. 전체 코퍼스가 얼마인지 vocab의 수가 얼마인지 등이 나온다.

model = Word2Vec.load("word2vec_1billion.model")
score, predictions = model.wv.evaluate_word_analogies('questions-words.txt')  
print(score)

# Compare accuracy by modifying hyper parameter

#기존의 word2vec
 Word2Vec(sentences, size=300, window=10, min_count=5, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.0001, iter=3) #score: 24%

#iter=4, workers=8 수정 
Word2Vec(sentences, size=300, window=10, min_count=5, 
                  workers=8, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.0001, iter=4) #score: 30.2%

#workers = 8 수정 
Word2Vec(sentences, size=300, window=10, min_count=5, 
                  workers=8, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.0001, iter=3) #score: 26%

#size=400 수정 
Word2Vec(sentences, size=400, window=10, min_count=5, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.0001, iter=3) # score: 26%

#window=5, min_count=7 수정 
Word2Vec(sentences, size=300  , window=5, min_count=7, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.0001, iter=3) # score: 24%
                  
#iter=4, min_alpha=0.001 수정 
Word2Vec(sentences, size=300, window=10, min_count=5, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.001, iter=4) #score: 31%

#size=500, min_count=3, min_alpha=0.001, iter=4 수정
model = Word2Vec(sentences, size=500, window=10, min_count=3, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.001, iter=4) #score: 30%

#size=500, window=5, min_count=3, min_alpha=0.001, iter=4 수정 
Word2Vec(sentences, size=500, window=5, min_count=3, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.001, iter=4) #score: 27%

#size=500, window=25,min_count=10, min_alpha=0.001, iter=4 수정 
Word2Vec(sentences, size=500, window=25, min_count=10, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.001, iter=4) #score: 36.9%

#size=700, window=25, min_count=10, min_alpha=0.001, iter=4 수정 
Word2Vec(sentences, size=700, window=25, min_count=10, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.001, iter=4) #score: 37.1%, time: 2970.
                  
#size=1000, window=25, min_count=10, min_alpha=0.001, iter=4 수정
Word2Vec(sentences, size=1000, window=25, min_count=10, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.001, iter=4) #score:36.5% time:3514.9617614746094

#size=1000, window=15, min_count=10, min_alpha=0.001, iter=4 수정 
Word2Vec(sentences, size=1000, window=15, min_count=10, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.001, iter=4) #score: 35% time: 3285.4314732551575

#size=500, window=25, min_count=5 iter=4, min_alpha=0.001
Word2Vec(sentences, size=500, window=25, min_count=5, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.001, iter=4) #score: 35.7%

#size=500, window=25, min_count=5, iter=4, min_alpha=0.001, workers=8
Word2Vec(sentences, size=500, window=25, min_count=5, 
                  workers=8, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.001, iter=4) #score: 35.8%

#size=800, window=40, min_count=15, iter=4, min_alpha=0.001
Word2Vec(sentences, size=800, window=40, min_count=15, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.001, iter=4) #score: 38.5%

#size=800, window=40, min_count=25, min_alpha=0.001, iter=4
Word2Vec(sentences, size=800, window=40, min_count=25, 
                  workers=4, sg=0, hs=0, negative=15, ns_exponent=0.75, 
                  cbow_mean=1, alpha=0.01, min_alpha=0.001, iter=4) #score: 39.5% time: 46분 -> 시간은 오래 걸렸지만 embedding size를 크게하고 window의 값도 크게하고 min_count도 크게 했더니 
                                                                    #정답률이 올라가는 것을 확인 할 수 있었다.