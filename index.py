import pyautogui
import time
time.sleep(10)
for line in open("text.txt", "r"):
    pyautogui.typewrite(line)

 