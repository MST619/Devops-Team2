alphabetList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
gameGridList = []

def gameGrid(xAxis,yAxis):
    #Start of code to create alphabetLine - First Line of game grid"
    alphabetLineContent = "  "
    alphabetLine = []
    i = 0
    while i < xAxis :
        alphabetLineContent += "   " + alphabetList[i] + "  "
        i+=1
    alphabetLineContent += " "
    alphabetLine.append(alphabetLineContent)
    gameGridList.append(alphabetLine) #add first line to grid list - e.g [   A     B     C     D     E   ]
    #End of code to create alphabetLine - First Line of game grid"

    #Start of code to create boundaryLine - game grid seperating lines"
    boundaryLineContent = "  "
    boundaryLine = []
    i = 0
    while i < xAxis :
        boundaryLineContent += "+-----"
        i+=1

    boundaryLineContent += "+"
    boundaryLine.append(boundaryLineContent)
    gameGridList.append(boundaryLine) #add second line to grid list -     e.g [+-----+-----+-----+-----+-----+]
    #End of code to create boundaryLine - game grid seperating lines"

    #Start of code to create grids
    i = 0
    while i < yAxis:
        row = []
        rowContent = ""
        if i < 9:
            row += ((" " + str(i+1) + "|     |") + (("     |") * (xAxis-1)))
        else:
            row += (("" + str(i+1) + "|     |") + (("     |") * (xAxis-1)))
        row.append(rowContent)
        gameGridList.append(row)
        gameGridList.append(boundaryLine)
        i+=1
        #End of code to create grids
      
    #Prints out game grid
    for line in gameGridList:
        print("".join(line))

    return (gameGridList)


#def buildingPool():
    

def newGame():
    print("Please select Game Map size \n")
    xAxis = int(input('Enter in your desired map size width: '))
    yAxis = int(input('Enter in your desired map size height: '))
    if (xAxis * yAxis <= 40):
        gameGrid(xAxis,yAxis)
    elif (xAxis * yAxis > 40):
        print("Grid is too big! Please keep within 40 squares")
        newGame()
    return xAxis, yAxis

def buildingPool():
    print("Please select 5 building types")
    