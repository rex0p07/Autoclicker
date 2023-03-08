import pyautogui
import threading
import time

# coordinates of the two positions to click
x1, y1 = 899, 476
x2, y2 = 815, 545

# delay between clicks (in milliseconds)
delay = 1

# function to run in the first thread
def click1():
    while True:
        pyautogui.click(x1, y1)
        time.sleep(delay / 1000)

# function to run in the second thread
def click2():
    while True:
        pyautogui.click(x2, y2)
        time.sleep(delay / 1000)

# create and start the threads
t1 = threading.Thread(target=click1)
t2 = threading.Thread(target=click2)
t1.start()
t2.start()
