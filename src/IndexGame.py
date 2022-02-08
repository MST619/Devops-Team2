'''
S10192803, Dickson Kuan, 
S10197943, Min Se Thu,
S10185214, Ethan Leong,
S10194816, Isaiah Low,
S10198398, Jeremiah Long

'''
#Imports
# <<<<<<< LoadGameData#3.2
# #import pandas as pd
# >>>>>>> CheckFile#3.1

# Global variables and imports

turn = 0
map = []
bch_score = []
fac_score = []
hse_score = []
shp_score = []
hwy_score = []
prk_score = []
mon_score = []
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
    #display 2 randomly selected building via selectedBuilding
    #display game menu options
    
    print("Under development")

def chooseBuildingPool():
    #To choose which building to build for building pool
    userchoices = []
    building1 = str(input("Please enter a desired building type (1/5): "))
    building2 = str(input("Please enter a desired building type (2/5): "))
    building3 = str(input("Please enter a desired building type (3/5): "))
    building4 = str(input("Please enter a desired building type (4/5): "))
    building5 = str(input("Please enter a desired building type (5/5): "))
    userchoices.extend((building1, building2, building3, building4, building5))
    for choice in userchoices:
        if choice not in buildingPool:
            print("Invalid input!")
            chooseBuildingPool()
        else:
            buildingPool[choice] = 8
    #Use global variable: BuildingPool Dictionary
    print(buildingPool)
    return buildingPool

def randomBuilding():
    randomSelectedBuilding = []
    #Return selected building in a list
    return randomSelectedBuilding

def buildBuildings(selectedBuilding):
    #Use global variable: Map
    #Update building location in the map
    print("Under development")

def bchcalc(map, bch_score):
#part for BCH calculation
    for xinput in range(len(map)):
    #if first column append 3
        if "BCH" in map[xinput][0]:
            bch_score.append(3)

        #if last column append 3
        if "BCH" in map[xinput][-1]:
            bch_score.append(3)

        #finding all the other BCH and adding 1 point
        for yinput in range((len(map[xinput]))):
            if yinput != 0 and yinput != len(map[xinput]) -1:
                if map[xinput][yinput] == "BCH":
                    
                    bch_score.append(1)
    bch_score_num = sum(bch_score)
    return bch_score_num

def faccalc(map, fac_score):
    fac_count = 0
    for xinput in range(len(map)):
    #finding all the FAC and reassign it’s value for calculation
        for yinput in range((len(map[xinput]))):
            if map[xinput][yinput] == "FAC":
                fac_count += 1

    if fac_count <= 4:
        fac_point = fac_count * fac_count
        fac_score.append(fac_point)
    if fac_count > 4:
        fac_count -= 4
        fac_point = 16 + fac_count
        fac_score.append(fac_point)

    fac_score_num = sum(fac_score)
    return fac_score_num

def hsecalc(map, hse_score):
    for xinput in range(len(map)):
        for yinput in range((len(map[xinput]))):
            if map[xinput][yinput] == "HSE":
                if (any(0 <= yinput + dyinput <= len(map) and 0 <= xinput + dxinput <= len(map[0]) \
                and map[xinput + dxinput][yinput + dyinput] == "FAC" \
                for dxinput, dyinput in ((-1, 0), (0,1), (1,0), (0,-1)))):
                    hse_score.append(1)

                if (any(0 <= yinput + dyinput <= len(map) and 0 <= xinput + dxinput <= len(map[0]) \
                and map[xinput + dxinput][yinput + dyinput] \
                for dxinput, dyinput in ((-1, 0), (0,1), (1,0), (0,-1)))):
                    gridList = []

                    if(not xinput + 1 > len(map)):
                        gridList.append(map[xinput + 1][yinput])
                    if(not xinput - 1 < 0):
                        gridList.append(map[xinput - 1][yinput])
                    if(not yinput + 1 > len(map[0])):
                        gridList.append(map[xinput][yinput + 1])
                    if(not yinput - 1 > 0):
                        gridList.append(map[xinput][yinput - 1])

        total_count = 0
        total_count += gridList.count("HSE")
        total_count += gridList.count("SHP")
        total_count += gridList.count("BCH")*2
        if(gridList.count != 0):
            hse_score.append(total_count)
    
    hse_score_num = sum(hse_score)
    return hse_score_num

def shpcalc(map, shp_score):
    for xinput in range(len(map)):
        for yinput in range(len(map)):
            if map[xinput][yinput] == "SHP":
                SHPgridList = (list(map[xinput + dxinput][yinput + dyinput]\
                for dxinput, dyinput in ((-1,0), (0,1), (1,0), (0,-1))))
        shp_score += len(set(SHPgridList))
    return shp_score

def hwycalc(map, hwy_score):
    for xinput in range(len(map)):
        hwy_chain = 0
        for yininput in range(len(map[xinput])):
            if map[xinput][yininput] == "HWY":
                if hwy_chain != 0:
                    hwy_chain -= 1
                    continue
            hwy_chain = 1
            ymove = yininput
            while True:
                if map[xinput][yininput][ymove + 1] == "HWY":
                    hwy_chain += 1
                    ymove += 1
                else:
                    break
        else:
            break
    if hwy_chain != 0:
        hwy_score.append(hwy_chain**2)
        hwy_chain -= 1

    hwy_score_num = sum(hwy_score)
    return hwy_score_num

def prkcalc(map , prk_score):
    for xinput in range(len(map)):
        for yinput in range(len(map)):
            if (any(0 <= yinput + dyinput <= len(map) and 0 <= xinput + dxinput <= len(map[0]) \
                and map[xinput + dxinput][yinput + dyinput] == "PRK" \
                for dxinput, dyinput in ((-1, 0), (0,1), (1,0), (0,-1)))):
                    gridList = []

                    if(not xinput + 1 > len(map[0])):
                        gridList.append(map[xinput + 1][yinput])
                    if(not xinput - 1 < 0):
                        gridList.append(map[xinput - 1][yinput])
                    if(not yinput + 1 > len(map)):
                        gridList.append(map[xinput][yinput + 1])
                    if(not yinput - 1 > 0):
                        gridList.append(map[xinput][yinput - 1])
                    total_count = 0
                    Set_score = 0
                    total_count += gridList.count("PRK")
                    
                    if (gridList.count == 0):
                        prk_score.append(Set_score)
                    if (gridList.count == 1):
                        Set_score = 1
                        prk_score.append(Set_score)
                    if(gridList.count == 2):
                        Set_score = 3
                        prk_score.append(Set_score)
                    if(gridList.count == 3):
                        Set_score = 8
                        prk_score.append(Set_score)
                    if(gridList.count == 4):
                        Set_score = 16
                        prk_score.append(Set_score)
                    if(gridList.count == 5):
                        Set_score = 22
                        prk_score.append(Set_score)
                    if(gridList.count == 6):
                        Set_score = 23
                        prk_score.append(Set_score)
                    if(gridList.count == 7):
                        Set_score = 24
                        prk_score.append(Set_score)
                    if(gridList.count >= 8):
                        Set_score = 25
                        prk_score.append(Set_score)

    prk_score_num = sum(prk_score)
    return prk_score_num

def moncalc(map, mon_score):
    Cornerscore = 0
    Moncalc = 0
    Index = 0
    for xinput in range(len(map)):
        if xinput == 0 or xinput == len(map)-1: 
        #if in the corner of the game grid add 2
            if "MON" == map[xinput][0]:
                Cornerscore += 1
                Index += 1
                Moncalc += 2

            if "MON" == map[xinput][-1]:
                Cornerscore += 1
                Index += 1
                Moncalc += 2
        
                
        #finding all the other MON and adding 1 point
        for yinput in range((len(map[xinput]))):
                if yinput != 0 and yinput != len(map[xinput]) -1:
                    if map[xinput][yinput] == "MON":
                        Index += 1
                        Moncalc += 1
            
    if Cornerscore >= 3:
        Moncalc = 4 * Index
            
    mon_score.append(Moncalc)
    mon_score_num = sum(mon_score)
    return mon_score_num

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

def remainingBuildings():
    #Use global variable: Building Pool
    for building, count in buildingPool.items():
        print(building, ':', count)
        return buildingPool

#2.2.2  Create game map list
def buildGameList(mapSize): 
    gameMap = []
    for x in range(mapSize[0]):
        holder = " " * int(mapSize[1])
        gameMap.append(list(holder))
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

def saveLeaderboard():
    #Load file and load data
    #Save new data into list
    #Save data into file
    print("Under development")

def playGame():
    while True:
        #Check if map is full and end the game
        randomSelectedBuildings = randomBuilding()
        displayGameMenu(turn, map, randomSelectedBuildings)
        userInput = input("Please enter option: ")
        if userInput == "0":
            #Check if user want to save game
            while True:
                userInput = input("Do you want to save your progress? Y/N: ")
                if userInput == "Y":
                    saveLeaderboard()
                    break
                elif userInput == "N":
                    break
                else:
                    print("Please enter a valid input")
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

def newGame():
    buildGameMap()
    chooseBuildingPool()
    playGame()

def checkFile(type):
    #Check Type
    filename = "LoadGame.csv"
    if type == "Leaderboard":
        filename = "leaderboard.csv"
    #find and load file
    try: 
        #Check game file #3.1
        # df = pd.read_csv(filename)
        counter = 0
        while True:
            for i in open(filename):
                #To strip the \n
                i = i.strip("\n")
                if counter == 0:
                    if(checkUserInputInt(i)!= True):
                        return False
                counter += 1
        return True
    except FileNotFoundError:
        print("cannot find file")
        return False

#Load data from file #3.2
def loadGame():
    #Check if file exsists
    if checkFile("LoadGame"):
        counter = 0
        buildingPoolDictionary ={ 
                "BCH":0, 
                "HSE":0,
                "SHP":0,
                "FAC":0,
                "HWY":0,
                "MON":0,
                "PRK":0
            }
        for x in open("LoadGame.py"):
            x= x.strip("\n")
            if counter == 0:
                turn = int(x)
            elif counter == 1:
                buildingPoolDictionary["BCH"] = int(x)
            elif counter == 2:
                buildingPoolDictionary["HSE"] = int(x)
            elif counter == 3:
                buildingPoolDictionary["SHP"] = int(x)
            elif counter == 4:
                buildingPoolDictionary["FAC"] = int(x)
            elif counter == 5:
                buildingPoolDictionary["HWY"] = int(x)
            elif counter == 6:
                buildingPoolDictionary["MON"] = int(x)
            elif counter == 7:
                buildingPoolDictionary["PRK"] = int(x)
            else:
                map.append(x.split(","))
            mapSize[1] += 1
        mapSize[0] = len(map[0])
    return mapSize, map, buildingPoolDictionary, turn

#File functions
def leaderBoard():
    #find and load file
    #display leaderboard list
    print("Under development")

def saveLeaderboard():
    #find and load file
    #create new file if cannot find file
    #Save data into file
    print("under development")

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

