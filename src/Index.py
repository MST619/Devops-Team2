'''
S10192803, Dickson Kuan, 
S10197943, Min Se Thu,
S10185214, Ethan Leong,
S10194816, Isaiah Low,
S10198398, Jeremiah Long

'''

import random
import Game

# Global lists and Variable 
map_Layout=[]
totalScore = 0

'''
Core Functions =========================================================================================================================================================

'''
# Feature 1.1
def menu():
	
	#Step 1: Print menu options
	print("Welcome, mayor of Simp City! \n------------------------------ \n1. Start new game \n2. Load saved game \n3. Show high scores \n\n0. Exit")

	#Step 2: Print to request for user input
	menuInput = input("Your Choice?")
	#Step 3: Return user input
	return menuInput

#Feature 3
def newGame(): 
	# print("To create new game map")
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

# Feature 4
def saveGame():
	print("To save game progress into CSV File")

# Feature 5
def InitLoad():
	print("To check for maze saved game")

def Exit():
	GameEnd = "Thanks for playing!"
	return GameEnd



'''
1. User GUI  =========================================================================================================================================================

'''
menuoption = menu()
while True:
	if menuoption == "0":
		exit = Exit()
		print(exit)
		break

	if menuoption == "1":
		userInput,GameMap,RandBuilding1,RandBuilding2,turn,buildings = newGame()
		while True:
			if turn > 16:
				menuoption = menu()
				break
			if userInput == "1":
				userInput,GameMap,RandBuilding1,RandBuilding2,turn,buildings = Game.printLayout(GameMap,RandBuilding1,turn,buildings)

			elif userInput == "2":
				userInput,GameMap,RandBuilding1,RandBuilding2,turn,buildings = Game.printLayout(GameMap,RandBuilding2,turn,buildings)

			elif userInput == "3":
				RandBuilding1, RandBuilding2, userInput = Game.viewRemaning(buildings)

			elif userInput == "0":
				menuoption = menu()
				break

			else:
				print("Invalid option.")
				userInput = input("Your Choice? ")
				continue
	
	else:
		print("Invalid option.")
		menuoption = menu()
		continue

