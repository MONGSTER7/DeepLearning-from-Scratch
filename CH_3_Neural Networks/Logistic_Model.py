# Logistic_Model 직접 만들어보기
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


y = np.array([1, 2])  # y.shape = 1*2

loss = np.mean((yp-y)**2)
print("loss:", loss)

# dw, db구하기

dw = 2*(x.T@(yp-y))  # (yp-y) = 1*2, x = 1*3, w =3*2 최종 w의 모양으로 만들어야한다.
                            # (yp-y)@x == 1*2 @ 1*3은 오류가 남. x를 전치시켜야한다. 업데이트과정에서 w - dw를 해야하기에 dw는 w와 같은 shape이어야함.
                            # 예를들어 크기를 맞춰 (yp-y).T@x 이런식으로 오차에 전치를 시키면 계산은 되지만, w의 shape 3*2의 모양이 아니다.
                            
db = 2*(yp-y)        # b의 크기는 1*2이므로 (yp-y)도 1*2의 모양이 되어야한다. 따라서 전치시킬 필요가 없다.


# update하기

lr = 0.1
w = w - lr*dw
b = b - lr*db