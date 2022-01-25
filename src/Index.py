'''
S10192803, Dickson Kuan, 
S10197943, Min Se Thu,
S10185214, Ethan Leong,
S10194816, Isaiah Low,
S10198398, Jeremiah Long

'''

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
            newGame()
        elif userInput == "2":
            print("Feature still under development!\n\n", end = '')
        elif userInput == "3":
            print("Feature still under development!\n\n", end = '')
        else:
            print("Invalid input!\n", end = '')
    

def newGame(): 
            # variables needed for gameplay:
            GameMap = [['','','',''],\
                        ['','','',''],\
                        ['','','',''],\
                        ['','','','']]
            
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
            print('Feature still in development!')
# code runs here

bch_score = [ ]
fac_score = [ ]
hse_score = [ ]
shp_score = [ ]
hwy_score = [ ]
prk_score = [ ]
mon_score = [ ]

def scorecalc(gameGridList):

#part for BCH calculation
    for xinput in range(len(gameGridList)):
	    #if first row append 3
	    if 'BCH' in gameGridList[xinput][0]:
		    bch_score.append(3)

	    #if last row append 3
		elif 'BCH' in gameGridList[xinput][-1]:
			bch_score.append(3)
		
		#finding all the other BCH and adding 1 point
		for yinput in range((len(gameGridList[xinput]))):
			if gameGridList[xinput][yinput] == 'BCH':
				bch_score.append(1)

    #finding all the FAC and reassign it’s value for calculation
	for yinput in range((len(gameGridList[xinput]))):
		if gameGridList[xinput][yinput] == 'FAC':
			fac_score.append(1)

	flattened_gameGridList = [val for sublist in gameGridList for val in sublist]
    	FAC_count = flattened_gameGridList.count("FAC")
	
	for i in range((len(FAC_count)):
		if i <= 4:
			fac_point = i * i
			fac_score.append(fac_point)
		elif i > 4:
			fac_count -= 4
			fac_point = 16 + fac_count #remaining value of fac’s
			fac_score.append(fac_point)
	
	#Finding all the HSE and checking around it (up down left right) for FAC
	if(gameGridList[xinput][yinput] == “HSE”:
		If (any(0 <= yinput + dyinput <= grid_column and 0 <= xinput + dxinput <= grid_row and gamegridlst[xinput + dxinput][yinput + dyinput] == “FAC” for dxinput, dyinput in ((-1, 0), (0,1), (1,0), (0,-1)))):
		hse_score.append(1)
	#Finding all the HSE and checking around it (up down left right) for remaining buildings for SHP or HSE
		elif (any(0 <= yinput + dyinput <= grid_column and 0 <= xinput + dxinput <= grid_row and gameGridList[xinput + dxinput][yinput + dyinput] for dxinput, dyinput in ((-1,0), (0,1), (1,0), (0,-1)))):
	#grid list would look like this [“?”,”HSE”,”?”,”?”]
	gridList = [ ]
	
	if(not xinput + 1 > grid_column):
		gridList.append(gameGridList[xinput + 1][yinput])
	if(not xinput - 1 < 0):
		gridList.append(gameGridList[xinput - 1][yinput])
	if(not yinput + 1 > grid_row):
		gridList.append(gameGridList[xinput][yinput + 1])
	if(not yinput - 1 > 0):
		gridList.append(gameGridList[xinput][yinput - 1])
	
	total_count = 0
	total_count += gridList.count(“HSE”)
	total_count += gridList.count(“SHP”)
	total_count += gridList.count(“BCH”)*2
	if(gridList.count != 0):
		hse_score.append(total_count)
#Finding all the SHP
	for xinput in range(len(gameGridList)):
		for yinput in range(len(gameGridList)):
			if gameGridList[xinput][yinput] = “SHP”:
				SHPgridList = (list(gameGridList[xinput + dxinput][yinput + dyinput] for dxinput, dyinput in ((-1,0), (0,1), (1,0), (0,-1))))
				score += len(set(SHPgridList))

	#Finding all the HWY
	for xinput in range(len(gameGridList)):
		HWYchain = 0
		for yinput in range(len(gameGridList[xinput])):
			if (‘HWY’ in gameGridList[xinput][yinput]):
				If HWYchain != 0:
					HWYchain -= 1
					continue
				HWYchain = 1
				yMove = yinput
				while True:
					if (gameGridList[xinput][yMove + 1] == “HWY”):
						HWYchain += 1
						yMove += 1
				else:
					Break
			else:
				break
		If HWYchain != 0:
			hwy_score+=HWYchain**2
			HWYchain -= 1

	#Finding all the PRK
	if(gameGridList[xinput][yinput] == “PRK”:
		If (any(0 <= yinput + dyinput <= grid_column and 0 <= xinput + dxinput <= grid_row and gamegridlst[xinput + dxinput][yinput + dyinput] == “PRK” for dxinput, dyinput in ((-1, 0), (0,1), (1,0), (0,-1)))):
	
	gridList = []

	if(not xinput + 1 > grid_column):
		gridList.append(gameGridList[xinput + 1][yinput])
	if(not xinput - 1 < 0):
		gridList.append(gameGridList[xinput - 1][yinput])
	if(not yinput + 1 > grid_row):
		gridList.append(gameGridList[xinput][yinput + 1])
	if(not yinput - 1 > 0):
		gridList.append(gameGridList[xinput][yinput - 1])
	total_count = 0
	Set_score = 0
	total_count += gridList.count(“PRK”)
	
	if (gridList.count == 0):
		prk_score.append(Set_score)
	if (gridList.count == 1):
		Set_score = 1
		prk_score.append(Set_score)
	elif(gridList.count == 2):
		Set_score = 3
		prk_score.append(Set_score)
	elif(gridList.count == 3):
		Set_score = 8
		prk_score.append(Set_score)
	elif(gridList.count == 4):
		Set_score = 16
		prk_score.append(Set_score)
	elif(gridList.count == 5):
		Set_score = 22
		prk_score.append(Set_score)
	elif(gridList.count == 6):
		Set_score = 23
		prk_score.append(Set_score)
	elif(gridList.count == 7):
		Set_score = 24
		prk_score.append(Set_score)
	elif(gridList.count >= 8):
		Set_score = 25
		prk_score.append(Set_score)

	#finding all the MON
	for xinput in range(len(gameGridList)):
		
		Cornerscore = 0
		Moncalc = 0
		Index = 0
	#if in the corner of the game grid add 2
	if 'MON' in gameGridList[xinput][0]:
		Cornerscore += 1
		Index += 1
		Moncalc += 2


		If “BCH” in gameGridList[xinput][-1]:
			Cornerscore += 1
			Index += 1
			Moncalc += 2
		
    If “MON” in gameGridList[xinput][0]:
	    Cornerscore += 1
	    Index += 1
		    Moncalc += 2
		
    If “MON” in gameGridList[xinput][0]:
	    Cornerscore += 1
	    Index += 1
		    Moncalc += 2
			
		#finding all the other MON and adding 1 point
		for yinput in range((len(gameGridList[xinput]))):
			If gameGridList[xinput][yinput] == “MON”:
				Index += 1
				Moncalc += 1
		
		If Cornerscore >= 3:
			Moncalc = 4 * index
		
		mon_score.append(Moncalc)

try:
    runMainMenu()
except:
    pass