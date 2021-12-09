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
try:
    runMainMenu()
except:
    pass