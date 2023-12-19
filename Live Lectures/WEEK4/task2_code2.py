import pyautogui
sc_Width, sc_Height = pyautogui.size()  #gets the Screen Resolution
 
pyautogui.press(['win'])                # pressing of arrow keys
pyautogui.press(['p','a','i','n','t'], interval=2)  #automating the pressing of arrow keys
pyautogui.press(['enter'])              #automating the pressing of arrow keys

pyautogui.moveTo(475,90,2)  # moves the mouse to the circle
pyautogui.click()           # mouse click function

pyautogui.moveTo(940,90,2)  # colour yellow
pyautogui.click()

pyautogui.moveTo(475,280,2) # canvas
pyautogui.mouseDown()

pyautogui.moveTo(675,480,2) # draw circle
pyautogui.mouseUp()

pyautogui.moveTo(275,90,2)  # fill icon
pyautogui.click()

pyautogui.moveTo(575,380,2) # canvas
pyautogui.click()

pyautogui.moveTo(813,90,2)  # colour yellow
pyautogui.click()

pyautogui.moveTo(475,90,2)  # circle icon
pyautogui.click()          

pyautogui.moveTo(540,340,2) # canvas
pyautogui.mouseDown()

pyautogui.moveTo(550,350,2) # canvas
pyautogui.mouseUp()

pyautogui.moveTo(640,340,2) # canvas
pyautogui.mouseDown()

pyautogui.moveTo(650,350,2) # canvas
pyautogui.mouseUp()

pyautogui.moveTo(460,90,2)  # swiggly line icon
pyautogui.click() 

pyautogui.moveTo(540,380,2) # canvas
pyautogui.mouseDown()

pyautogui.moveTo(650,380,2) # canvas
pyautogui.mouseUp()

pyautogui.moveTo(600,430,2) # canvas
pyautogui.click()

pyautogui.moveTo(300,90,2)  # text icon
pyautogui.click() 

pyautogui.moveTo(700,380,2) # canvas
pyautogui.click()

creator = "by Stewart Blakeway"
age = "aged nevermind"
pyautogui.press(list(creator) + ["enter"] + list(age), interval=2)

im2 = pyautogui.screenshot('my_master_piece.png') # taking screenshot of the current window and save it
          