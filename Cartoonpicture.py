import sys

import cv2
import numpy
import pyautogui as pg
#Cartooning images
img='D:\\Projects\\Projects\\py.jpg'
def cartooning():
    image=cv2.imread(img)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray=cv2.medianBlur(gray, 5)
    edges=cv2.adaptiveThreshold(gray,255,
                                cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY,9,9)

    #CARTONATION
    color=cv2.bilateralFilter(image,9,250,250)
    cartoon=cv2.bitwise_and(color,color,mask=edges)

    cv2.imshow('image',image)
    cv2.imshow('edges',edges)
    cv2.imshow('cartoon',cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# def camera():
#     # camera
#     import cv2

#     image = cv2.VideoCapture(0)

#     while (True):
#         success, frame = image.read()
#         frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
#         cv2.imshow('Camera', frame)
#         C = cv2.waitKey(1)
#         if C == 27:
#             break
#     image.release()
#     cv2.destroyAllWindows()

if __name__ == '__main__':
    a=pg.confirm('Are you sure about cartooning your picture', buttons=['Yes', 'No'])
    if a=='Yes':
        cartooning()
    else:
        sys.exit()


