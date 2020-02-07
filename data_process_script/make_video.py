import cv2
import numpy as np
import os
img_dirs ="./vis_crowd_choice"



list_name = os.listdir("./vis_crowd_choice")

for name in list_name:
    name = os.path.join(img_dirs,name)
    img = cv2.imread(name)
    print(img.shape)