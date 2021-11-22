'''
S10192803, Dickson Kuan, 
S10197943, Min Se Thu,
S10185214, Ethan Leong,
S10194816, Isaiah Low,
S10198398, Jeremiah Long

'''

import random
#from typing_extensions import TypeVarTuple

# Global lists and Variable 
map_Layout=[]
totalScore = 0

'''
Core Functions =========================================================================================================================================================

'''
# Feature 1.1
def menu():
	# Step 1: Print menu options
	print("Welcome, mayor of Simp City! \n------------------------------ \n1. Start new game \n2. Load saved game \n3. Show high scores \n\n0. Exit")

	# Step 2: Print to request for user input
	menuInput = input("Your Choice?\n")

	# Step 3: Return user input
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
	print("Turn {}".format(turn));

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
7. Game Function =========================================================================================================================================================
'''

# Feature 7.1 
def printLayout(GameMap, buildings, turn, newBuilding):
	# print("To print the game layout")
	check = True
	while check:
		validation = ["A1","A2","A3","A4","B1","B2","B3","B4","C1","C2","C3","C4","D1","D2","D3","D4"]
		userInput = input('Build where? \n')
		userInput = userInput.upper()
		if userInput in validation:
	# Feature 7.2 
	# Find user input location to place the building
			locList = [['A',0],['B',1],['C',2],['D',3]]
			for row in locList:

				if userInput[0] in row:
					location = [int(userInput[1])-1,row[1]]

					if (GameMap[location[0]] [location[1]] == ''):
						validInput = False

						if (0 <= location[0] + 1 < len(GameMap[0])):
							if (GameMap[location[0] + 1][location[1]] != ""):
								validInput = True

						if (0 <= location[0] - 1 < len(GameMap[0])):
							if (GameMap[location[0] - 1][location[1]] != ""):
								validInput = True

						if (0 <= location[1] + 1 < len(GameMap)):
							if (GameMap[location[0]][location[1] + 1] != ""):
								validInput = True

						if (0 <= location[1] - 1 < len(GameMap)):
							if (GameMap[location[0]][location[1] - 1] != ""):
								validInput = True

						if validInput == True or turn == 1:
							GameMap[location[0]][location[1]] = newBuilding[buildings][0]
							check = False
						else:
							print('You must place an existing building')
					else:
						print('This location already has a building, please choose another location.')
		else:
			print("Please provide a valid input")
			continue

	# display turns
	turn += 1

	# building randomizer
	RandBuilding1 = random.randint(0,4)
	RandBuilding2 = random.randint(0,4)

	buildingCode = ['HSE','FAC','SHP','HWY','BCH']

	newBuilding[buildings][1] -= 1

	while True:
		if newBuilding[RandBuilding1][1] <= 0:
			RandBuilding1 = random.randint(0,4)
			continue
        
		if newBuilding[RandBuilding2][1] <= 0:
			RandBuilding2 = random.randint(0,4)
			continue
        
		break

	if turn <= 16:
		print('Turn {}'.format(turn))
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

		return userInput,GameMap,RandBuilding1,RandBuilding1,turn,newBuilding

#Feature 7.3

#Feature 7.4
def calculateScore():
	print("Calculate total score via the number of buildings")

'''
6. Leaderboard Function =========================================================================================================================================================

'''
def loadLeaderBoard():
	print("To load leaderboard data into CSV")
	#Step 1: Check exsisting leaderboard CSV file
	#Step 2.1: Create new leaderboard CSV file
	#Step 2.2: Load CSV data into list
	#Step 3: return data list

def createLeaderboardFile():
	print("If there is no leaderboard CSV file, create leaderboard file")

def saveLeaderboard():
	print("To save leaderboard scores into a csv file")
	#Step 1: Load leaderboard CSV file
	leaderBoardData = loadLeaderBoard('Leaderboard.csv');
	#Step 3: Add data into list
	#Step 4: Save list into CSV file (Either overwrite or add on)

def printLeaderboard():
	print("print leaderboard")
	#Step 1: Load leaderboard CSV file
	#Step 2: Print leaderboard

'''
1. User GUI  =========================================================================================================================================================

'''
while True:
	menuoption = menu()
	pass
	if menuoption == "0":
		Exit()
		break

	if menuoption == "1":
		userInput,GameMap,RandBuilding1,RandBuilding2,turn,buildings = newGame()
		while True:
			if turn > 16:
				menu()
				break
			if userInput == "1":
				userInput,GameMap,RandBuilding1,RandBuilding2,turn,buildings = printLayout(GameMap,RandBuilding1,turn,buildings)

			elif userInput == "2":
				userInput,GameMap,RandBuilding1,RandBuilding2,turn,buildings = printLayout(GameMap,RandBuilding2,turn,buildings)

			elif userInput == "0":
				menu()
				break

			else:
				print("Invalid option.")
				userInput = input("Your Choice? ")
				continue