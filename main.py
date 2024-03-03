import cv2
import mediapipe as mp
import time
import handTrackingModule as htm
import numpy as np
import math

wcam, hcam = 640, 480

#############################
# code for system volume control
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volumeRange = volume.GetVolumeRange()

minVol = volumeRange[0]
maxVol = volumeRange[1]
#############################

cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)
ptime =0
flag = True

detector = htm.handDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        #print(lmList[4],lmList[8])
        x1 , y1 = lmList[4][1], lmList[4][2]
        x2 , y2 = lmList[8][1], lmList[8][2]
        x3 , y3 = lmList[9][1], lmList[9][2]
        x4 , y4 = lmList[12][1], lmList[12][2]
        cx ,cy = (x1+x2)//2 , (y1+y2)//2

        length_for_mute = math.hypot(x3-x4, y3-y4)
        length = math.hypot(x2-x1, y2-y1)
        #print(length)

        cv2.circle(img, (cx,cy), 10, (255,0,0), cv2.FILLED)
        cv2.circle(img, (x1,y1), 5, (0,0,255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 5, (0,0,255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255,0,255), 3)

        #hand range 30 160
        #volume range -63 0
        if(flag == True):
            vol = np.interp(length, [30,160], [minVol, maxVol])
            #print(vol)
            volume.SetMasterVolumeLevel(vol, None)
        if length_for_mute < 20:
            cv2.circle(img, (x3,y3), 10, (0,255,0), cv2.FILLED)
            time.sleep(0.25)
            flag = not flag
            
        if length < 50:
            cv2.circle(img, (cx,cy), 10, (0,255,0), cv2.FILLED)

        cv2.putText(img, str(flag), (20, 80), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

    cTime = time.time()
    fps = 1/(cTime-ptime)
    ptime = cTime

    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

    #img = cv2.flip(img, 1)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
