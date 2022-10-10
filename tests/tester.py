import time
from automation.single_message_sender import single_thread_sender

# Location Info
[first_message_x, first_message_y] = [113, 375] #Data generated from Cursor Method

message_in_one_screen = 9
distance_of_two_threads = 55


def tester():
    print("Testing will be started within 5 seconds. Place your cursour")
    time.sleep(5)

    [cur_x,cur_y] = [first_message_x,first_message_y]

    for i in range (0,message_in_one_screen):
        print(f"Current Mouse at ({cur_x},{cur_y})")
        single_thread_sender(cur_x,cur_y,False)
        time.sleep(1)
        cur_y+=distance_of_two_threads