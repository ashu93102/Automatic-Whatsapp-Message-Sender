import pyautogui
import time

while True:
    time.sleep(5)
    x,y = pyautogui.position()
    print(x,y)
