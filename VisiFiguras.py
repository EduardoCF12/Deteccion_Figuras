
import cv2 as cv
from cv2 import resize
from cv2 import FONT_HERSHEY_COMPLEX_SMALL as Fuente
import numpy as np

ima = cv.imread('estrella3.png')
img = resize(ima, dsize = (500,500), interpolation = cv.INTER_CUBIC)
gris = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img = cv.erode(gris, None, iterations=1)
img = cv.Canny(image=img, threshold1=127, threshold2=100)
img = cv.blur(img, ksize=(5,5))


contor,_ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

for i in contor:
	e = 0.01*cv.arcLength(i,True)
	aprx = cv.approxPolyDP(i,e,True)
	x,y,w,h = cv.boundingRect(aprx)

if len(aprx) == 4:

    cv.putText(img, text='Es un cuadrado', org=(20,40), fontFace = Fuente, fontScale=1, color=(255,255,255), thickness=4, lineType=cv.LINE_8)

if len(aprx) == 10:

    cv.putText(img, text='Es una estrella', org=(20,40), fontFace = Fuente, fontScale=1, color=(255,255,255), thickness=4, lineType=cv.LINE_8)

if len(aprx) > 10:

    cv.putText(img, text='Es un circulo', org=(20,40), fontFace = Fuente, fontScale=1, color=(255,255,255), thickness=4, lineType=cv.LINE_8)


cv.imshow('ima',img)
cv.waitKey(0)