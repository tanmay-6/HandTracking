Dependencies required
1- OpenCV // for getting realtime images (video)
2- mediapipe // for tracking palm and fingers
3- pycaw // for controlling volume

Details of some of funtions used...
**cv2.VideoCapture(0):** This is a function call to the VideoCapture() function from the cv2 module. 
This function is used to capture video from a source, such as a webcam or a video file. 
The parameter 0 passed to it indicates the index of the camera device to use. In this case, 
0 typically refers to the default camera connected to your system. If you have multiple cameras, you can use different indices to select a specific camera.

**cap.read():** This method is called on the cv2.VideoCapture object cap. It reads a single frame from the video capture device (cap) and returns two values:
success: A boolean value indicating whether the frame was successfully captured (True) or not (False).
img: The captured frame, represented as a NumPy array (or None if the capture was unsuccessful).

**cv2.imshow("Image", img):** This function displays an image in a window. It takes two parameters:
"Image": The title of the window.
img: The image to be displayed, which is the frame captured from the video.
**cv2.waitKey(1):** This function waits for a specified amount of time for a keyboard event. It takes one parameter:
1: The time to wait in milliseconds. Here, it waits for 1 millisecond.
This function is necessary to keep the window open and responsive. If you don't call cv2.waitKey(), 
the window may close immediately after opening, as the program execution would continue.

**mp.solutions.hands** is imported and assigned to mpHands, giving access to the hand tracking functionality.
**mpHands.Hands()** creates an instance of the hand tracking model, which can then be used to detect and track hands in images or video frames.

**mpDraw.draw_landmarks():** This function draws the landmarks and connections on the image. It takes three parameters:
img: The original image on which the landmarks and connections will be drawn.
handLMs: The landmarks of the hand to be drawn.
mpHands.HAND_CONNECTIONS: This parameter specifies the connections between the landmarks, which will also be drawn. 
It's a predefined constant provided by MediaPipe that represents the connections between different hand landmarks.
