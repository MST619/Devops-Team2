import random
'''
7. Game Function =========================================================================================================================================================
'''

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

# Feature 7.2 
# Find user input location to place the building
def inputLocationValidation(userInput):
	validation = ["A1","A2","A3","A4","B1","B2","B3","B4","C1","C2","C3","C4","D1","D2","D3","D4"]
	if userInput in validation:
		return True
	else:
		return False

def checkLocList(userInput):
	locList = [['A',0],['B',1],['C',2],['D',3]]
	for row in locList:
		if userInput in row:
			return row[1]
	return None

def checkValidInput(GameMap,location):
	if (0 <= location[0] + 1 < len(GameMap[0])):
		if (GameMap[location[0] + 1][location[1]] != ""):
			return True

	if (0 <= location[0] - 1 < len(GameMap[0])):
		if (GameMap[location[0] - 1][location[1]] != ""):
			return True

	if (0 <= location[1] + 1 < len(GameMap)):
		if (GameMap[location[0]][location[1] + 1] != ""):
			return True

	if (0 <= location[1] - 1 < len(GameMap)):
		if (GameMap[location[0]][location[1] - 1] != ""):
			return True

	return False

def checkBuildingLeft(newBuilding):
	# to check if there is any building left
	while True:
		RandBuilding = random.randint(0,4)
		if newBuilding[RandBuilding][1] <= 0:
			continue
        
		return RandBuilding
		# if newBuilding[RandBuilding2][1] <= 0:
		# 	RandBuilding2 = random.randint(0,4)
		# 	continue
        
		

# Feature 7.1
def printLayout(GameMap, buildings, turn, newBuilding):
	# print("To print the game layout")
	check = True
	while check:
		userInput = input('Build where? \n')
		userInput = userInput.upper()
		if inputLocationValidation(userInput):
			checkLocListResult = checkLocList(userInput[0])
			if checkLocListResult != None:
				location = [int(userInput[1])-1,checkLocListResult]
				print(location)
				if (GameMap[location[0]] [location[1]] == ''):
					if checkValidInput(GameMap, location) == True or turn == 1:
						GameMap[location[0]][location[1]] = newBuilding[buildings][0]
						check = False
					else:
						print('You must place near an existing building')
				else:
					print('This location already has a building, please choose another location.')
					continue
					
		else:
			print("Please provide a valid input")

	# display turns
	turn += 1

	# building randomizer
	buildingCode = ['HSE','FAC','SHP','HWY','BCH']

	newBuilding[buildings][1] -= 1
	RandBuilding1 = checkBuildingLeft(newBuilding)
	RandBuilding2 = checkBuildingLeft(newBuilding)

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

		return userInput,GameMap,RandBuilding1,RandBuilding2,turn,newBuilding

#Feature 7.2
def viewRemaning(newBuilding):
	print("{:<30}{:<20}".format("Building","Remaining"))
	print("{:<30}{:<20}".format("--------","--------"))
	for count in range(len(newBuilding)):
		print("{:<30}{:<20}".format(newBuilding[count][0],newBuilding[count][1]))

	#Options
	buildingCode = ['HSE','FAC','SHP','HWY','BCH']
	RandBuilding1 = random.randint(0,4)
	RandBuilding2 = random.randint(0,4)
	print(' 1. Build a {}'.format(buildingCode[RandBuilding1]), '\n', '2. Build a {}'.format(buildingCode[RandBuilding2]), '\n', '3. See remaining buildings\n','4. See current score\n\n','5. Save game\n','0. Exit to main menu')
	userInput = input('Your choice?\n')
	return RandBuilding1, RandBuilding2, userInput

#Feature 7.3

#Feature 7.4
def calculateScore():
	print("Calculate total score via the number of buildings")
	return ""

def userInput():
	x = input()
	return x
