import cv2
import numpy as np
import pyautogui
image = pyautogui.screenshot()
# image = cv2.imread('ss.jpg')
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
crop_img = image[350:1050, 280:780]
# cv2.imshow("cropped", crop_img)
# cv2.waitKey(0)
cv2.imwrite('ss.jpg', crop_img)
