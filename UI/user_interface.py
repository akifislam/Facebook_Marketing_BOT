# © Akif Islam | 2022 | github.com/akifislam

from automation.cursor_detection import detect_cursor
from tests.tester import tester
from automation.bulk_sender import bulk_sender

def load_ui():
    print("Hi,\nWe have the following services for you.\n\nPlease type 1,2 or 3 to check that option :\n")
    print("____________\n")
    print("1. Bulk Message Sender\n2. Bulk Message Tester\n3. Detect Cursor Location")
    print("\n\nIn case of emergency exit, please move your mouse cursour to the top right corner\n")
    print("________\n\n")

    user_input = 1
    try:
        user_input = int(input("Enter your choice :\n"))
    except:
        print("Please enter a valid choice\n")
        user_input = int(input("Enter your choice"))

    if(user_input==1):
        bulk_sender()
    elif(user_input==2):
        tester()
    elif(user_input==3):
        detect_cursor()










