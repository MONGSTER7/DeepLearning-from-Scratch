# yp예측값 구하기, shape을 확인하며 

import numpy as np
x = np.array([[1.0, 2.0, 3.0]])
w = np.array([[1,2],[3,4],[5,6]])
b = np.array([1,2])
print("x.shape:", x.shape)    # 3*1
print("w.shape:", w.shape)    # 3*2
print("b.shape:", b.shape)    # (3,)

yp = np.dot(x,w) + b  # 여기서 xw,wx 내적 순서에따라 값이 달라짐. x@w가 맞다.
print("yp.shape:", yp.shape)  # yp.shape =  1*3 @ 3*2 = 1*2
print(yp)