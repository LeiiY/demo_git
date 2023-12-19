# --- My Test Based Adventure Game ---
import time, os

def file_reader():
	playerSettings = list()
	with open("settings.txt") as file:
		playerSettings = file.readlines()

	playerSettings = [line.rstrip('\n') for line in open("settings.txt")]
	file.close()
	return playerSettings

def file_saver():
	with open ("settings.txt", "w") as file:
		for item in playerSettings:
			file.write("%s\n" % item)
	time.sleep(2)
	print("Game Saved...\n")

def file_changer():
	settingChange = int(input("What do you want to change? "))
	newValue = input("What is the new setting? ")
	playerSettings[settingChange - 1] = newValue

def welcome():
	print("Welcome to my game " + playerSettings[0] + "\nPlease choose a character: ")

	characterList = ["Knight", "Warrior", "Wizard"]

	for idx, val in enumerate(characterList, start = 1):
		print(" " + str(idx) + ". " + val)

	character = int(input("Type in your character number: "))
	playerSettings[1] = characterList[character - 1]

	print("You chose: " + playerSettings[1])

def movement():
	move = input("\n" + playerSettings[1] + ", do you want to move? ")

	count = 0
	while move in ('Yes', 'yes', 'YES', 'y', 'Y'):
		print("You moved forwards 1 space!")
		move = input("Keep moving? ")
		count += 1
	else:
		print("You moved " + str(count) + " spaces. Congrats!")
		playerSettings[3] = int(playerSettings[3]) + count
		file_saver()

def menu_system():
	if (menu == 1):
		movement()
	elif (menu == 2):
		file_changer()
	elif (menu == 3):
		print("Name: %s \nCharacter Name: %s \nCharacter Age: %s" % (playerSettings[0], playerSettings[1], playerSettings[2]))
	elif (menu == 4):
		file_saver()
	elif (menu == 5):
		os._exit(0)			
	else:
		print("Not a valid input! Try again!")		

# Actual Game Play Starts Here
print("Loading. . . .")
time.sleep(2)
playerSettings = file_reader()

while True:
	menu = int(input("\nWould you like to start the adventure (1), change settings (2), view settings (3), save game (4) or exit (5)? "))

	try:
		if not menu in range(1, 6):
			print("Choose either 1, 2, 3, 4 or 5")
		else:
			menu_system()	
	except:	
		print("Choose either 1, 2, 3, 4 or 5")