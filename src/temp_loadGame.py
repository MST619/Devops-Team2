def getFile(file_Name):
    while True:
        try:
            # Open the file 
            file = open(file_Name)
            # Declaring variables
            turns = 0
            list = []
            x_counter = 0
            y_counter = 0 
            buildingPool = {
                "BCH":5, 
                "HSE":5,
                "SHP":5,
                "FAC":5,
                "HWY":5,
                "MON":5,
                "PRK":5
            }

            #read file line
            for x in file:
                holder = x.strip('\n')

                #To get turn number 
                if turns == 0:
                    turns = int(holder)
                else:
                    list.append(list(holder))
                    #count the number of line for x and y axis
                    x_counter += 1
                    y_counter = len(holder)

            #Checking building used
            for x in x_counter:
                for y in y_counter:
                    #check if element in the building pool
                    if list[x][y] in buildingPool:
                        buildingPool[list[x][y]] = buildingPool[list[x][y]] - 1

            return list, turns, x_counter, y_counter, buildingPool

        except FileNotFoundError:
            print("File not found")
            file_Name = input("Please re-enter the name of the file, else type 0 to exit: ")
            if file_Name == 0:
                return 0
