# # 자료형 변경 astype
import numpy as np
x = np.array([-1.0, 1.0, 2.0])
print(x)

y = x>0 # bool형으로 변환하여 True, False로 출력
print(y)

y = y.astype(int)
print(y)
