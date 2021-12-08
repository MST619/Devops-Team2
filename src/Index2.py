'''
S10192803, Dickson Kuan, 
S10197943, Min Se Thu,
S10185214, Ethan Leong,
S10194816, Isaiah Low,
S10198398, Jeremiah Long

'''

import random
import Game
import sys
MainMenuData = \
['Welcome, mayor of Simp City!',
'------------------------------',
'1. Start new game',
'2. Load saved game',
'3. Show high scores\n'
'0. Exit']

def displayMainMenu():
    for i in range(len(MainMenuData)):
            print(MainMenuData[i])
   
def runMainMenu():
    displayMainMenu()
    userInput = input('Enter your option: ')
    MainMenuSelection(userInput)

# Exit the game  
def exitGame():
	GameEnd = "Thanks for playing!"
	return GameEnd

def MainMenuSelection(userInput):
    if userInput == "0":
        exit = exitGame()
        print(exit)
        sys.exit()
    elif userInput == "1":
        print("Feature still under developent!")
    elif userInput == "2":
        print("Feature still under developent!")
    elif userInput == "3":
        print("Feature still under development!")
    else:
        print("Invalid input!")

# code runs here
runMainMenu()