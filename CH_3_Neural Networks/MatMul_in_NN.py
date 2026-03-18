# # 신경망에서의 행렬 곱
import numpy as np

x = np.array([1, 2])  # 입력 벡터
print("x.shape:", x.shape)

w = np.array([[1, 3, 5], [2, 4, 6]])
print(w)

y = np.dot(x, w)       # 여기서 두 행렬을 내적할 때 넘파이가 x를 1*2형태(1행2열)로 자동 변환하여 계산한다.
print("y:", y)
