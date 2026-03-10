#1.56 원소 접근

import numpy as np
X = np.array([[51, 55], [14, 19], [0, 4]])

for row in X:   #row는 X 자체가 넘파이 배열(np.array)이기 때문에, 그 안에서 꺼내온 한 줄도 똑같이 넘파이 배열 형태를 유지합니다.
   print(row)
