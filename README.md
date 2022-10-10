# Facebook Marketing BOT
(Documentation will be updated soon. This is just copied from the previous one)

## Behind the Story
Suppose,
- Mr.A was a single guy from the last 10 years 
- He has knocked over 1000+ girls on Facebook Messanger.
- Only 25 of them responded and he tried to flirt with all of them.

Let's say they are Ms. A, Ms. B, Ms. C ... upto Ms.Y.
- But, Unfortunately, after a few days of flirting, everyone of them cheated on him.
- Now finally, he has got the love his life (and also his wife) ' Ms. Z '  on his 26th attempt.
- But he doesn't want his wife to know about his previous conversations.
- Nowadays, sometimes, his wife checks his messanger. So he wants to delete his all the previous conversations from messanger. But is it possible to delete all those 1000+ shits manually? Probably, a big NO.

So, here comes the solution, a simple few line python scripts run without requiring any kind of Facebook email, password or authentication. 
</br>

Steps to Follow
- Open your 'Facebook Messanger for Desktop' App.
- Place the cursor on the first chat of your messanger from where you want to start deleting. Suppose, I want to keep my last 50 person's chat. So I will place the cursor on 51th person's name.
- Run the detect_cursor( ) method detect your mouse cursor position

It will return something like [230,160] where (x,y) =(230,160)
```python
def detect_cursor():
    time.sleep(6)
    print("Waiting to setup a position...")
    location = [pyautogui.position().x, pyautogui.position().y]
    print("Mouse position detected at : ", pyautogui.position())
    return location
```
## Demonstration
Finally, Grab a Popcorn or a Diet-Coke and run the main method, you will see something like this :

<center>
    <img src="./Sample/Sample_DeleteFBMessages.gif">
</center>

### Created with ❤️ by Akif Islam
