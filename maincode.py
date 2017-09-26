import numpy as np
import cv2
import os

def binaryzation(img_1):
    GrayImag =cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY) 
    k,img_2 = cv2.threshold(GrayImag,150,255,cv2.THRESH_BINARY)
    cv2.imwrite('aim.png',img_2)
    return img_2

def YellowProportion(img_1):
    imgarray = np.array(img_1)
    count = 0
    index = imgarray.shape
    #print(index)
    for i in range(index[0]):
        for j in range(index[1]):
            if imgarray[i][j] == 0:
                count += 1
    allnum = imgarray.size
    print(count,allnum)
    return 1.0 - count / allnum            
                
def main():
    Img_1 = cv2.imread('E:\\Microsoft VS Code\\MyPython\\Demo_1\\test.png',2|4)
    Img_3 = cv2.medianBlur(Img_1,5)
    Img_2 = binaryzation(Img_3)
    final = YellowProportion(Img_2)
    print(final)
    #cv2.imshow('asd.png',Img_2)
    #os.system('pause')
    return None

if __name__ == '__main__':
    main()


