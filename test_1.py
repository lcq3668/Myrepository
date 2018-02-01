# -*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot
if __name__=='__main__': 
    im1=cv2.imread('C:\Users\Public\Pictures\Sample Pictures\Koala.jpg',cv2.IMREAD_COLOR)
    cv2.namedWindow('image1', cv2.WINDOW_AUTOSIZE)    #第二个参数可以为  WINDOW_AUTOSIZE,  或WINDOW_NORMAL；
                                                        # 若果是前者，则窗口不能随意缩放，为后者，则可随心缩放
    cv2.imshow('image1',im1)
    # k=cv2.waitKey(0)
    # print k
    # if k == 27:         # wait for ESC key to exit
        # cv2.destroyAllWindows()
    # elif k == ord('s'): # wait for 's' key to save and exit
        # cv2.imwrite('kola.png',img)
        # cv2.destroyAllWindows()
    pyplot.imshow(im1, cmap = 'gray', interpolation = 'bicubic')
    #pyplot.xticks([]), pyplot.yticks([])  # to hide tick values on X and Y axis
    pyplot.show()