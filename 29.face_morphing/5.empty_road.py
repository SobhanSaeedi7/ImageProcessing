import numpy as np
import cv2
from skimage import data, filters
 

cap = cv2.VideoCapture('Inputs\cars.mp4')
 
frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)
 

frames = []
for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    _, frame = cap.read()
    frames.append(frame)
 
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)    
 

cv2.imwrite("Outputs/empty_road.jpg", medianFrame)