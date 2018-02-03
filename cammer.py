#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
# This is a tiny example that shows how to show live images from Nao using OpenCV.  
  
import sys  
import cv2 as cv  
from cv2 import COLOR_RGB2BGRA
from naoqi import ALProxy  
import vision_definitions  
from numpy import array
from PIL import Image
class OpenCVModule():  
    def __init__(self, IP, PORT, CameraID):  
        print CameraID
        self._videoProxy = None  
        self._cameraID = CameraID  
        self._resolution = vision_definitions.kQVGA  # 320 * 240  
        self._colorSpace = vision_definitions.kBGRColorSpace  
        self._fps = 20  
        self._imgClient = ""  
        self._imgData = None  
        cv.namedWindow("Camera_OpenCV", 0)  
        self._registerImageClient(IP, PORT)  
  
    def _registerImageClient(self, IP, PORT):  
        self._videoProxy = ALProxy("ALVideoDevice", IP, PORT)  
        self._imgClient = self._videoProxy.subscribeCamera("OpenC", 0, self._resolution, self._colorSpace,self._fps)  
        print self._imgClient
    def _unregisterImageClient(self):  
        if self._imgClient != "":  
            self._videoProxy.unsubscribe(self._imgClient)  
  
    def showImage(self):  
        while True:  
            try:  
                self._imgData = self._videoProxy.getImageRemote(self._imgClient)  
                width=self._imgData[0]
                height=self._imgData[1]
                #self._img=array(self._imgData[6]).astype(int)
                ima_data=self._imgData[6]
                Nao_ima=Image.frombytes('RGB',(width,height),ima_data)
                Nao_ima=cv.cvtColor(array(Nao_ima),COLOR_RGB2BGRA)
                cv.imshow("Camera_OpenCV2", Nao_ima)  
            except KeyboardInterrupt:  
                break  
            except:  
                pass  
            if cv.waitKey(20) == 27:
                break
        cv.DestroyAllWindows()  
        self._unregisterImageClient()  
  
if __name__ == '__main__':  
    IP = "192.168.1.105"   
    PORT = 9559  
    CameraID = 0  
    if len(sys.argv) > 1:  
        IP = sys.argv[1]  
    if len(sys.argv) > 2:  
        CameraID = int(sys.argv[2])  
    myWidget = OpenCVModule(IP, PORT, CameraID)  
    myWidget.showImage()  