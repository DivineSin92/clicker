from pyautogui import *
import pyautogui
import time

def click_img():
    location = pyautogui.locateOnScreen('click.png', confidence = 0.75)
    pyautogui.click(location)

def is_on_screen():
    if pyautogui.locateOnScreen('click.png', confidence = 0.75) != None:
        click_img()
        return False
    else:
        time.sleep(0.5)
        return True

while is_on_screen():
    is_on_screen()
