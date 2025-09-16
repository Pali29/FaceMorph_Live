import pyvirtualcam as pvc
import cv2
import numpy as np

video = cv2.VideoCapture(0)

ret, frame = video.read()
height, width, _ = frame.shape


cam = pvc.Camera(width, height, fps=30)
print(f'Using virtual camera: {cam.device}')
while True:
    ret, frame = video.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cam.send(frame_rgb)
    cam.sleep_until_next_frame()