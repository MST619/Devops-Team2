'''
S10192803, Dickson Kuan, 
S10197943, Min Se Thu,
S10185214, Ethan Leong,
S10194816, Isaiah Low,
S10198398, Jeremiah Long

'''

# Global variables and imports
turn = 0
map = []
#Building pool dictionary
buildingPool = { 
                "BCH":0, 
                "HSE":0,
                "SHP":0,
                "FAC":0,
                "HWY":0,
                "MON":0,
                "PRK":0
            }
mapSize = [0,0]  #X-axis, Y-axis

# General functions
def displayMainMenu():
    return True

def checkUserInputInt(value): #to check if the user input is able to conver to int
    try:
        int(value)
        return True
    except ValueError:
        return False

def checkUserInputString(value): #to check if the user input is able to conver to string
    try:
        str(value)
        return True
    except ValueError:
        return False

#Game functions
def displayGameMenu(turn, map, selectedBuilding):
    #display turns
    #display building remaining
    #display map
    #display 2 randomly selected building
    #display game menu options
    
    print("Under development")

def chooseBuildingPool():
    #To choose which building to build for building pool
    #Use global variable: BuildingPool Dictionary
    print("under development")

def randomBuilding():
    randomSelectedBuilding = []
    #Return selected building in a list
    return randomSelectedBuilding

def buildBuildings(selectedBuilding):
    #Use global variable: Map
    #Update building location in the map
    print("Under development")

def calculateScore():
    #Use global varibale: Building Pool
    #calculateScore for each building
    buildingScore = []
    #Return building score via int list
    return buildingScore

def displayScore():
    #Use global varibale: Building Pool
    score = calculateScore()
    #Print score
    print("Under development")

def buildGameList(mapSize):
    xCounter = yCounter = 0
    gameMap = []
    while mapSize[0] == xCounter:
        while mapSize[1] == yCounter:
            print("Under development")
            #Append list ","

    return gameMap  

def buildGameMap():
    #Build game map
    x = "1"
    y = "1"
    while checkUserInputInt(x):
        x = input("Please enter x-axis: ")
    while checkUserInputInt(y):
        y = input("Please enter y-axis: ")
    #Global var: mapSize
    mapSize=[x,y] #X-axis, Y-axis

    #Build game list
    map = buildGameList(mapSize)

def newGame():
    buildGameMap()
    chooseBuildingPool()
    while True:
        #Check if map is full and end the game
        randomSelectedBuildings = randomBuilding()
        displayGameMenu(turn, map, randomSelectedBuildings)
        userInput = input("Please enter option: ")
        if userInput == "0":
            break
        elif checkUserInputInt(userInput):
            userInput = int(userInput)
            if userInput == 1 and userInput == 2:
                buildBuildings(randomSelectedBuildings[userInput-1])
            elif userInput == 3:
                break
        else:
            print("please eneter a valid input")
    #To calculate and display score
    displayScore()
    #Put score into leaderboard file

def loadGame():
    #find and load file
    #Put the apporiate data into the global var
    return True

#File functions
def leaderBoard():
    #find and load file
    #display data
    displayScore()

    return True

# UI
def mainMenu():
    while True:
        displayMainMenu()
        userInput = input("Please enter option: ")
        
        #Check if user input is valid
        if userInput > 3 and checkUserInputInt(userInput) != True:
            if userInput == "0":
                print("Thanks for playing!")
                break
            elif userInput == "1":
                newGame()
            elif userInput == "2":
                loadGame()
            elif userInput == "3":
                leaderBoard()
        else: 
            print("Please enter a valid user input")