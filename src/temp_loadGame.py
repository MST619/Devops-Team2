def getFile(file_Name):
    while True:
        try:
            file = open(file_Name)
            turns = 0
            list = []
            #read file line
            counter = 0
            for x in file:
                holder = x.strip('\n')

                #To get turn number 
                if counter == 0:
                    turns = int(holder)
                else:
                    list.append(list(holder))

                #count the number of line
                counter += 1

        except FileNotFoundError:
            print("File not found")
            file_Name = input("Please re-enter the name of the file, else type 0 to exit: ")
            if file_Name == 0:
                return 0
