'''
S10192803, Dickson Kuan, 
S10197943, Min Se Thu


'''
#Global lists and Variable 
map_Layout=[]
totlaScore = 0

'''
Core Functions =========================================================================================================================================================

'''

def menu():
	print("This is to print menu functions")
	menu=["Start new game", "Load saved game", "Exit"]
	#Step 1: Print menu options

	#Step 2: Print for user inptu
	print("Your choice?")
def InitLoad():
	print("To check for maze saved game")

def printLayout():
	print("To print the game layout")

def saveGame():
	print("To save game progress into CSV File")

def newGame():
	print("To create new game map")

'''
Game Function =========================================================================================================================================================

'''
def updateLocation():
	print("To add buildings into speicfic spots")

def calculateScore():
	print("Calculate total score via the number of buildings")

'''
Leaderboard Function =========================================================================================================================================================

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
User GUI  =========================================================================================================================================================

'''
while True:
	option = menu()
	pass