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

            

        except FileNotFoundError:
            print("File not found")
            file_Name = input("Please re-enter the name of the file, else type 0 to exit: ")
            if file_Name == 0:
                return 0
