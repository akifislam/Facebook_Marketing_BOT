import pyautogui
import time
from automation.column_sender import send_message_in_column
import math

# Location Info
[first_message_x, first_message_y] = [113, 375] #Data generated from Cursor Method

message_in_one_screen = 9
no_of_persons = 20
scroll_distance = -30

def bulk_sender():
    time.sleep(5)
    for messageCount in range (0,math.ceil(no_of_persons/message_in_one_screen)):
        send_message_in_column()
        pyautogui.moveTo(first_message_x,first_message_y)
        pyautogui.scroll(scroll_distance)