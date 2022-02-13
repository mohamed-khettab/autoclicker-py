from pynput import keyboard
from pynput.keyboard import *
import sys
import time
import pyautogui

running=True
notClicking=True
resume_key=Key.up
stop_key=Key.down
exit_key=Key.esc


def on_press(key):
    global running, notClicking
    if key==resume_key:
        notClicking=False
        print("Clicking started. Trying to click at " + str(divisor) + "CPS, might not be accurate.")
    if key==stop_key:
        print("Clicking stopped.")
        notClicking=True
    if key==exit_key:
        print("OK. Exiting.")
        time.sleep(1)
        sys.exit()
    

def helps():
    global delayed, divisor

    print("What would you like the clicks per second to be? (Might be very unaccurate!!)")
    print("WARNING: A CPS value too high might cause lag.")
    divisor=input()
    try:
        divisor=float(divisor)
    except:
        print("You did not enter a number. Exiting in 5 seconds.")
        time.sleep(5)
        sys.exit()
    if divisor<1:
        print("Number too small! Exiting in 5 seconds.")
        time.sleep(5)
        sys.exit()
    if divisor>100:
        print("Number too large. Exiting in 5 seconds.")
        time.sleep(5)
        sys.exit()
    print("OK. CPS value set to " + str(divisor))
    delayed=float()
    delayed=1/divisor  
    print("Press the up arrow to start clicking. Press the down arrow to stop. Press the ESC key to exit.")


def main():
    
    listener1=Listener(on_press=on_press)
    listener1.start()

    helps()

    while running:
        if not notClicking:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE=delayed
    listener1.stop()

    
if __name__=="__main__":
    main()
