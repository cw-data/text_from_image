"""
Automate the screenshot and next-page process

Requirements
1. Confirm that kindle app is open
2. user needs to manually set kindle window size and font size
3. Program should take screenshot, save screenshot to user-provided folder
4. Then program should hit right-key to advance page
5. How will program know the "correct" number of screenshots to take?
    - user provides `n` argument
"""

# take a screenshot from python
# https://stackoverflow.com/questions/2846947/get-screenshot-on-windows-with-python

# key-press from python

# pyautogui can do both, screenshot and key-press
# https://pyautogui.readthedocs.io/en/latest/screenshot.html
import pyautogui
import time
import random

endpage = 35 # endpage
i=0  # startpage; it's good to manually screenshot the 1st page since it has a picture
wait = 5
print('You have {wait} seconds to before first screenshot...')
time.sleep(wait)
while i <= endpage:
    w = random.uniform(int(1),int(2))
    w2 = random.uniform(int(1),int(2))
    print(f'Capturing page {i} of {endpage} after {round(w,1)} sec')
    time.sleep(w)
    im = pyautogui.screenshot(imageFilename=f'data/hp/ch3/pg{i}.png',region=(125,150, 1025, 1225))
    pyautogui.press('right')
    time.sleep(w2)
    i+=1
