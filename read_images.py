import os, time
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

images_dict = {}

# list images in /images folder
for file in os.listdir("./images"):
    if file.endswith(".webp"):
        print(file)
        image = cv2.imread("./images/" + file, cv2.IMREAD_COLOR)
        images_dict[file] = np.asarray(image)

window_name = "Main View"
view_window = cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)

# These two lines will force your "Main View" window to be on top with focus.
cv2.setWindowProperty(window_name,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty(window_name,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_NORMAL)

for key in images_dict.keys():
    print(key)
    
    cv2.imshow(window_name, images_dict[key])
    cv2.waitKey(150)


