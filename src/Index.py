'''
S10192803, Dickson Kuan, 
S10197943, Min Se Thu,
S10185214, Ethan Leong,
S10194816, Isaiah Low,
S10198398, Jeremiah Long

'''

import gameinit

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
    result = 1
    while result != 0:
        displayMainMenu()
        userInput = input('Enter your option: ')
        result = MainMenuSelection(userInput)
        

# Exit the game  
def exitGame():
	GameEnd = "Thanks for playing!"
	return GameEnd

def MainMenuSelection(userInput):
        if userInput == "0":
            exit = exitGame()
            print(exit)
            return 0
        elif userInput == "1":
            gameinit.newGame()
        elif userInput == "2":
            print("Feature still under development!\n\n", end = '')
        elif userInput == "3":
            print("Feature still under development!\n\n", end = '')
        else:
            print("Invalid input!\n", end = '')
    

try:
    runMainMenu()
except:
    pass