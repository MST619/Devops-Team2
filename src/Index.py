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
        displayMainMenu()
        userInput = input('Enter your option: ')
        print("You have selected option " + userInput)
        result = MainMenuSelection(userInput)
        return result
        

# Exit the game  
def exitGame():
	GameEnd = "Thanks for playing!"
	return GameEnd

def MainMenuSelection(userInput):
        if userInput == "0":
            exit = exitGame()
            print(exit)
            return userInput
        elif userInput == "1":
            newGame()
            return userInput
        elif userInput == "2":
            print("Feature still under development!", end = '')
            return userInput
        elif userInput == "3":
            print("Feature still under development!", end = '')
            return userInput
        else:
            print("Invalid input!", end = '')
            return userInput
    

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
def init_game():
    loop = True
    while loop:
        result = runMainMenu()
        if result == "0":
            loop = False
init_game()