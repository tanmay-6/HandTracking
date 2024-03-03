import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxhands=2 , detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxhands = maxhands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        #hand detection initialization here
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxhands)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img , draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        if (self.result.multi_hand_landmarks):
            for handLMs in self.result.multi_hand_landmarks:
                if(draw):
                    self.mpDraw.draw_landmarks(img,handLMs,self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if (self.result.multi_hand_landmarks):
            myHand = self.result.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h,w,c = img.shape
                cx ,cy = int(lm.x*w) , int(lm.y*h)

                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img,(cx,cy),5,(0,0,255),cv2.FILLED)
                    #cv2.putText(img,str(id),(cx,cy), cv2.FONT_HERSHEY_COMPLEX , 1, (0,255,0), 3)
        return lmList



#copy this code to your file
def main():
    #import cv2
    #import mediapipe as mp
    #import time
    #import handTrackingModule as htm

    cap = cv2.VideoCapture(0)
    pTime = 0
    cTime = 0

    detector = handDetector()
    while True:
        success , img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_COMPLEX , 1, (250,0,255), 3)
        
        #to flip the image
        #img = cv2.flip(img, 1)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()