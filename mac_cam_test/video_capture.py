import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)  # 0 refers to the device index or you could pass a video file instead
# 0 refers to the first camera, 1 to the second, 2 to the third, etc.
# This creates a video capture objects, which in the end needs to be released! (like any stream...)


fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # The argument is the codec or encoding for the video
out = cv2.VideoWriter('newcam.avi', fourcc, 20.0, (1280, 720))  # filename, fourcc, fps, frame size


for i in range(60):
    ret, frame = cap.read()  # ret is a bool indicating success
    # print(cap.get(3), cap.get(4))  # Tells us frame size
    print(frame.shape)
    if ret:
        #frame = cv2.flip(frame, 0)  # Flips the frame vertically - just for fun

        out.write(frame)

    else:
        break

    time.sleep(0.05) #  Notice that 1/0.05 = 20 \neq 80, so in fact I am speeding the video up by a factor of 4



cap.release()
out.release()