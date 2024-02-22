import pywhatkit as kit
import keyboard
import time
import pandas as pd
import pyautogui

# Change file path according to your data file path
data = pd.read_csv("message_file.csv").to_dict(orient="records")

for i in data:
    number = i["phone"]
    msg = i["message"]
    kit.sendwhatmsg_instantly(phone_no=f"+91{number}", message=msg)
    time.sleep(40)
    pyautogui.click(x=582, y=699)
    keyboard.press_and_release('enter')
    time.sleep(3)
    keyboard.press_and_release("Ctrl + w")

