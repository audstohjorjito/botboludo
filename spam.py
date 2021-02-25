#pito
#nico tu vieja viene fallada de fabrica tincho trolo

import pyautogui, time

time.sleep(3)
f = open ("spamdic2.txt", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
