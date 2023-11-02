from pyautogui import *
import pyautogui
import time
import requests

def message():
    token = ''
    chat_id = ''
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    parms = {'chat_id': chat_id, 'text': 'come back'}
    requests.get(url, params = parms)

def click_img():
    location = pyautogui.locateOnScreen('click.png', confidence = 0.75)
    pyautogui.click(location)

def is_on_screen():
    if pyautogui.locateOnScreen('click.png', confidence = 0.75) != None:
        click_img()
        message()
        return False
    else:
        time.sleep(0.5)
        return True

while is_on_screen():
    is_on_screen()
