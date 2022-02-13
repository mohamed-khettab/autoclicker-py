from pynput import keyboard
import pyautogui
import sys
import time

clicking=False
clicksps=float()
clickingkey=Key.shift_l
exitkey=Key.esc


def controls():
  global clicksps
  
  print("Enter the clicks per second you would like to click at.")
  print("WARNING: A high clicks per second value may cause lag.") 
  divisor=input()
  try:
    divisor=float(divisor)
  except:
    print("You did not enter a number!")
    print("Closing in 5 seconds.")
    time.sleep(5)
    sys.exit()
  if divisor>100:
    print("This number is larger than 100 and may cause extreme lag! Are you SURE?")
    print("y/n")
    choice=input()
    if choice=="y":
      continue
    if choice=="n":
      print("OK. Closing the program in 5 seconds.")
      time.sleep(5)
      sys.exit()
    if choice not "y" or "n":
      print("Invalid answer. Closing in 5 seconds.")
    if divisor<1:
        print("Number too small! Closing in 5 seconds.")
        time.sleep(5)
        sys.exit()
   clickps=1/divisor
   print("OK. Trying to click at " + str(divisor))
   print("Higher CPS values might not be accurate.")
   print("Press Left Shift to start clicking")
   print("Press it again to stop.")
   print("If you're experiencing errors, press esc to close the program.")

def on_press(Key):
  global clickingkey, exitkey
  
  if Key==clickingkey:
    if clicking=True:
      print("OK. Stopped clicking.")
      clicking=False
    else:
      print("OK. Clicking.")
      clickingkey=True
  if Key==exitkey:
    print("Closing the program.")
    sys.exit()

def main():
  listener1=Listener(on_press=on_press)
  listener1.start()
  controls()
  while clicking=True:
    pyautogui.click()
    pyautogui.PAUSE = clicksps


if __name__=="__main__":
  main()

