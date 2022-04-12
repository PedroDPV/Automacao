import pyautogui
import time
pyautogui.PAUSE = 1.5
time.sleep(1)

for n in range(3):
    pyautogui.position()
    print(pyautogui.position())
    time.sleep(2)




"""Point(x=1073, y=726)
Point(x=956, y=727)
Point(x=318, y=667)
"""
