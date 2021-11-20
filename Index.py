'''
S10192803, Dickson Kuan, 
S10197943, Min Se Thu,
S10185214, Ethan Leong,
S10194816, Isaiah Low,
S10198398, Jeremiah Long

'''
#Global lists and Variable 
map_Layout=[]
totlaScore = 0

'''
Core Functions =========================================================================================================================================================

'''
#Feature 1.1
def menu():
	#Step 1: Print menu options
	print("Welcome, mayor of Simp City! \n------------------------------ \n1. Start new game \n2. Load saved game \n3. Show high scores \n\n0. Exit")

	#Step 2: Print to request for user input
	userInput = input("Your Choice?")

	#Step 3: Return user input
	return userInput

#Feature 3
def newGame(): 
	print("To create new game map")
	
	GameMap = [['','','',''],\
				['','','',''],\
				['','','',''],\
				['','','','']]
	# building randomizer
	RandBuilding1 = random.randint(0,4)
	RandBuilding2 = random.randint(0,4)

	# buildings of 8 copies each
	buildingcopies = [['HSE',8],['FAC',8],['SHP',8],['HWY',8],['BCH',8]]
	# building code for referencing
	buildingcode = ['HSE','FAC','SHP','HWY','BCH']

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
	print('1. Build a {}'.format(buildingcode[RandBuilding1]), '\n', '2. Build a {}'.format(buildingcode[RandBuilding2]), '\n', '3. See remaining buildings\n','4. See current score\n\n','5. Save game\n','0. Exit to main menu')
	userChoice = input('Your choice?')

	#returning choice, map, building randomizer, turns and number of copies
	return userChoice, GameMap, RandBuilding1, RandBuilding2, turn, buildingcopies

#Feature 4
def saveGame():
	print("To save game progress into CSV File")

#Feature 5
def InitLoad():
	print("To check for maze saved game")

def Exit():
	print("Thanks for playing!")

'''
7. Game Function =========================================================================================================================================================
'''

#Feature 7.1 
def printLayout():
	print("To print the game layout")

#Featuer 7.2 
def updateLocation():
	print("To add buildings into speicfic spots")

#Featuer 7.3
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
	if menuoption == '0':
		Exit()
		break
