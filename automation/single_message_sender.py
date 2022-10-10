import pyautogui
import time

# Location Info

[inbox_text_field_x,inbox_text_field_y]=[657,758]

time_delay = .2




def single_thread_sender(message_x, message_y,is_active=True):
    time.sleep(time_delay)
    print(f"Clicking at {message_x,message_y}")
    time.sleep(time_delay)
    pyautogui.moveTo(message_x, message_y)
    time.sleep(time_delay)
    pyautogui.leftClick()
    time.sleep(time_delay)
    pyautogui.moveTo(inbox_text_field_x,inbox_text_field_y)
    time.sleep(time_delay)
    pyautogui.leftClick()
    time.sleep(time_delay)
    pyautogui.keyDown('command')
    time.sleep(.5)
    pyautogui.press('v')
    time.sleep(.5)
    pyautogui.keyUp('command')
    time.sleep(time_delay)

    if(is_active):
        pyautogui.press('enter')
    return [message_x,message_y]