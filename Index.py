'''
S10192803, Dickson Kuan, 
S10197943, Min Se Thu,
S10185214, Ethan Leong,
S10194816, Isaiah Low,

'''
#Global lists and Variable 
map_Layout=[]
totlaScore = 0

'''
Core Functions =========================================================================================================================================================

'''
#Feature 1.1
def menu():
	print("This is to print menu functions")
	menu=["Start new game", "Load saved game", "Exit"]
	#Step 1: Print menu options

	#Step 2: Print to request for user input
	print("Your choice?")

	#Step 3: Return user input

#Feature 3
def newGame():
	print("To create new game map")

#Feature 4
def saveGame():
	print("To save game progress into CSV File")

#Feature 5
def InitLoad():
	print("To check for maze saved game")

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
	option = menu()
	pass
