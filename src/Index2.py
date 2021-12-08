'''
S10192803, Dickson Kuan, 
S10197943, Min Se Thu,
S10185214, Ethan Leong,
S10194816, Isaiah Low,
S10198398, Jeremiah Long

'''

import random
import Game
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
    elif userInput == "1":
        print("Feature still under development!", end = '')
    elif userInput == "2":
        print("Feature still under development!", end = '')
    elif userInput == "3":
        print("Feature still under development!", end = '')
    else:
        print("Invalid input!", end = '')
    

def newGame(): 
            # variables needed for gameplay:
            GameMap = [['','','',''],\
                        ['','','',''],\
                        ['','','',''],\
                        ['','','','']]
            # building randomizer
            RandBuilding1 = random.randint(0,4)
            RandBuilding2 = random.randint(0,4)

            # buildings of 8 copies each    
            buildings = [['HSE',8],['FAC',8],['SHP',8],['HWY',8],['BCH',8]]
            # building code for referencing
            buildingCode = ['HSE','FAC','SHP','HWY','BCH']
            
            turn = 1
            print("Turn {}".format(turn))

            # Board creation (X and Y coordinates, placing the +, - and |)
            print("{:>5}{:>6}{:>6}{:>6}".format("A", "B", "C", "D"))
            for row in range(len(GameMap)):
                column = len(GameMap[row]) #defining the columns
                print(' ' + '+-----'*column+'+')
                print(row+1, end = '')
                for line in range(len(GameMap[row])): #defining the rows
                    print('|{:^5}'.format(GameMap[row][line]), end = '')
                print('|')
            print(' ' + '+-----'*column + '+')

            # Menu options
            print(' 1. Build a {}'.format(buildingCode[RandBuilding1]), '\n', '2. Build a {}'.format(buildingCode[RandBuilding2]), '\n', '3. See remaining buildings\n','4. See current score\n\n','5. Save game\n','0. Exit to main menu')
            userInput = input('Your choice?\n')

            # returning choice, map, building randomizer, turns and number of copies
            return userInput, GameMap, RandBuilding1, RandBuilding2, turn, buildings
# code runs here
runMainMenu()