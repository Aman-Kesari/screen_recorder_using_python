from win32api import GetSystemMetrics
import cv2
import time
import pyautogui
import numpy as np
width=GetSystemMetrics(0)
height=GetSystemMetrics(1)
dimension=(width,height)
format=cv2.VideoWriter_fourcc(*'MP4V')
filename=input("Enter filename : ")
output=cv2.VideoWriter(filename+".mp4",format,10.0,dimension)
start_time=time.time()
duration=int(input("Enter duration : "))
end_time=start_time+(duration *1.5)
print("Screen Recording Started !")
while True:
    shots=pyautogui.screenshot()
    video=np.array(shots)
    op_video=cv2.cvtColor(video,cv2.COLOR_BGR2RGB)
    output.write(op_video)
    current_time=time.time()
    if current_time>end_time:
       break
output.release()
print("Screen Recording Finished !")