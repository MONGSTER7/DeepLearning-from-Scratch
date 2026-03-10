# 1.63 이미지 표시하기
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('deeplearning/pokemon.png') # 이미지 읽어오기(적절한 경로를 설정하세요!)

plt.imshow(img)
plt.show()