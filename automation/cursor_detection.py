import pyautogui
import time

def detect_cursor():
    print("Waiting 5 seconds to setup a position...")
    time.sleep(5)
    location = [pyautogui.position().x, pyautogui.position().y]
    print("Mouse position detected at : ", pyautogui.position())
    return location