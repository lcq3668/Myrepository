# -*- coding: utf-8 -*-  
import cv2 as cv
from cv2 import IMREAD_COLOR
from numpy import array
guession=[[[255 for i in range(320)] for i in range(240)] for k in range(3)]
temp_store=array(guession).astype(int)


real_image=cv.imread(r'C:\Users\Public\Pictures\Sample Pictures\Koala.jpg',IMREAD_COLOR)
#print real_image
cv.imwrite(r'D:\studyINF\AI\2.7code\opencv\Koala.jpg',real_image)
cv.waitKey(0)