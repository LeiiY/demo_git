import pyautogui
sc_Width, sc_Height = pyautogui.size()  #gets the Screen Resolution

pyautogui.press(['win'])
pyautogui.press(['p','a','i','n','t'], interval=2)
pyautogui.press(['enter'])

pyautogui.moveTo(475,90,2)  
pyautogui.click()           
