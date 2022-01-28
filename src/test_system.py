from os import error
import pytest
import time

#====================================== START OF SYSTEM BEHAVIOR TESTING ====================================

def test_ExitAfterGameSetup_Pass1(monkeypatch):
    inputList = ["1","1","2","3","4","5","5","5","0","0"]
    start_time = time.time()
    print("Beginning Exit After Game Setup Test (Correct Inputs)")
    # Select Main Menu Option (1)
    # Choose Building Pool (1,2,3,4,5)
    # Choose Grid Size (5,5)
    # Exit to Main Menu (0)
    # Exit Program (0)
    try:
        inputs = iter(inputList)
        #Iterate through predefined inputs
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        #Run the game code
        import IndexGame
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Exit After Game Setup Passing Test took %s seconds to complete" % (time.time() - start_time))

def test_ExitAfterGameSetup_Fail1(monkeypatch):
    inputList = ["1",
                "/","-1","a"," ",
                "1","2","3","4","5",
                "/","-1","a"," ","5",
                "/","-1","a"," ","5",
                 "/","-1","a"," ","0",
                 "/","-1","a"," ","0"]
    start_time = time.time()
    print("Beginning Exit After Game Setup Test (Invalid Inputs)")
    # Select Main Menu Option (1)
    # Choose Building Pool [Invalid Inputs:(/,-1,a," ")] [Correct Inputs:(1,2,3,4,5)]
    # Choose Grid Size X axis [Invalid Inputs:(/,-1,a," ")] [Correct Input:(5)]
    # Choose Grid Size Y axis [Invalid Inputs:(/,-1,a," ")] [Correct Input:(5)]
    # Exit to Main Menu [Invalid Inputs:(/,-1,a," ")][Correct Inputs: 0]
    # Exit Program [Invalid Inputs:(/,-1,a," ")][Correct Inputs: 0]
    try:
        inputs = iter(inputList)
        #Iterate through predefined inputs
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        #Run the game code
        import IndexGame
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Exit After Game Setup Failing Test took %s seconds to complete" % (time.time() - start_time))

def test_ExitAfterGameSetup_Pass2(monkeypatch):
    inputList = ["1",
                "1","2","3","4","5",
                "10",
                "10",
                "0",
                "0"]
    start_time = time.time()
    print("Beginning Exit After Game Setup Test (Correct Inputs)")
    # Select Main Menu Option (1)
    # Choose Building Pool (1,2,3,4,5)
    # Choose Grid Size X axis [Invalid Inputs:(/,-1,a," ")] [Correct Input:(10)]
    # Choose Grid Size Y axis [Invalid Inputs:(/,-1,a," ")] [Correct Input:(10)]
    # Exit to Main Menu [Invalid Inputs:(/,-1,a," ")][Correct Input:(0)]
    # Exit Program [Invalid Inputs:(/,-1,a," ")][Correct Input:(0)]
    try:
        inputs = iter(inputList)
        #Iterate through predefined inputs
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        #Run the game code
        import IndexGame
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Exit After Game Setup Passing Test took %s seconds to complete" % (time.time() - start_time))

def test_ExitAfterGameSetup_Fail2(monkeypatch):
    inputList = ["1",
                "/","-1","a"," ","1","2","3","4","5",
                "/","-1","a"," ","10",
                "/","-1","a"," ","10",
                 "/","-1","a"," ","0",
                 "/","-1","a"," ","0"]
    start_time = time.time()
    print("Beginning Exit After Game Setup Test (Invalid Inputs)")
    # Select Main Menu Option (1)
    # Choose Building Pool [Invalid Inputs:(/,-1,a," ")] [Correct Inputs:(1,2,3,4,5)]
    # Choose Grid Size X axis [Invalid Inputs:(/,-1,a," ")] [Correct Input:(10)]
    # Choose Grid Size Y axis [Invalid Inputs:(/,-1,a," ")] [Correct Input:(10)]
    # Exit to Main Menu [Invalid Inputs:(/,-1,a," ")][Correct Inputs: 0]
    # Exit Program [Invalid Inputs:(/,-1,a," ")][Correct Inputs: 0]
    try:
        inputs = iter(inputList)
        #Iterate through predefined inputs
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        #Run the game code
        import IndexGame
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Exit After Game Setup Failing Test took %s seconds to complete" % (time.time() - start_time))

def test_ExitAfterNewGameFirstMove1_Pass(monkeypatch):
    inputList = ["1",
                "1","2","3","4","5",
                "5","5",
                "1",
                "1","1",
                "0",
                "0"]
    start_time = time.time()
    print("Beginning Exit After New Game First Move Random Building 1 Test (Correct Inputs)")
    # Select Main Menu Option (1)
    # Choose Building Pool [Correct Inputs:(1,2,3,4,5)]
    # Choose Grid Size X-Axis [Correct Inputs:(5)]
    # Choose Grid Size Y-Axis [Correct Inputs:(5)]
    # Choose Place Random Building 1 [Correct Inputs: 1]
    # Choose X axis for building [Correct Inputs: 1]
    # Choose Y axis for building [Correct Inputs: 1]
    # Exit to Main Menu [Correct Inputs: 0]
    # Exit Program [Correct Inputs: 0]
    try:
            inputs = iter(inputList)
            #Iterate through predefined inputs
            monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            #Run the game code
            import IndexGame
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Exit After New Game First Move Passing Test took %s seconds to complete" % (time.time() - start_time))

def test_ExitAfterNewGameFirstMove1_Fail(monkeypatch):
    inputList = ["1",
                "/","-1","a"," ","1","2","3","4","5",
                "/","-1","a"," ","5",
                "/","-1","a"," ","5",
                "/","-1","a"," ","1",
                "/","-1","a"," ","1",
                "/","-1","a"," ","1",
                "/","-1","a"," ","0",
                "/","-1","a"," ","0"]
    start_time = time.time()
    print("Beginning Exit After New Game First Move Random Building 1 Test (Wrong Inputs)")
    # Select Main Menu Option (1)
    # Choose Building Pool [Invalid Inputs:(/,-1,a," ")] [Correct Inputs:(1,2,3,4,5)]
    # Choose Grid Size X-Axis [Invalid Inputs:(/,-1,a," ")] [Correct Input:(5)]
    # Choose Grid Size Y-Axis [Invalid Inputs:(/,-1,a," ")] [Correct Input:(5)]
    # Choose Place Random Building 1 [Correct Input: 1]
    # Choose X axis for building [Invalid Inputs:(/,-1,a," ")] [Correct Input: 1]
    # Choose Y axis for building [Invalid Inputs:(/,-1,a," ")] [Correct Input: 1]
    # Exit to Main Menu [Correct Input: 0]
    # Exit Program [Correct Input: 0]
    try:
            inputs = iter(inputList)
            #Iterate through predefined inputs
            monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            #Run the game code
            import IndexGame
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Exit After New Game Fist Move Failing Test RandBulding1 took %s seconds to complete" % (time.time() - start_time))


def test_ExitAfterNewGameFirstMove2_Pass(monkeypatch):
    inputList = ["1",
                "1","2","3","4","5",
                "5",
                "5",
                "2",
                "1",
                "1",
                "0",
                "0"]
    start_time = time.time()
    print("Beginning Exit After New Game First Move RandBuilding2 Test (Correct Inputs)")
    # Select Main Menu Option (1)
    # Choose Building Pool [Correct Inputs:(1,2,3,4,5)]
    # Choose Grid Size X-Axis [Correct Input:(5)]
    # Choose Grid Size Y-Axis [Correct Input:(5)]
    # Choose Place Random Building 2 [Correct Input: 2]
    # Choose X axis for building [Correct Input: 1]
    # Choose Y axis for building [Correct Input: 1]
    # Exit to Main Menu [Correct Input: 0]
    # Exit Program [Correct Input: 0]
    try:
            inputs = iter(inputList)
            #Iterate through predefined inputs
            monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            #Run the game code
            import IndexGame
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Exit After New Game First Move Passing Test RandBulding2 took %s seconds to complete" % (time.time() - start_time))

def test_ExitAfterNewGameFirstMove2_Fail(monkeypatch):
    inputList = ["1",
                "/","-1","a"," ","1","2","3","4","5",
                "/","-1","a"," ","5",
                "/","-1","a"," ","5",
                "/","-1","a"," ","2",
                "/","-1","a"," ","1",
                "/","-1","a"," ","1",
                "/","-1","a"," ","0",
                "/","-1","a"," ","0"]
    start_time = time.time()
    print("Beginning Exit After New Game First Move Random Building 2 Test (Wrong Inputs)")
    # Select Main Menu Option (1)
    # Choose Building Pool [Invalid Inputs:(/,-1,a," ")] [Correct Inputs:(1,2,3,4,5)]
    # Choose Grid Size X-Axis [Invalid Inputs:(/,-1,a," ")] [Correct Inputs:(5)]
    # Choose Grid Size Y-Axis [Invalid Inputs:(/,-1,a," ")] [Correct Inputs:(5)]
    # Choose Place Random Building 1 [Invalid Inputs:(/,-1,a," ")] [Correct Inputs: 1]
    # Choose X axis for building [Invalid Inputs:(/,-1,a," ")] [Correct Inputs: 1]
    # Choose Y axis for building [Invalid Inputs:(/,-1,a," ")] [Correct Inputs: 1]
    # Exit to Main Menu [Invalid Inputs:(/,-1,a," ")] [Correct Inputs: 0]
    # Exit Program [Invalid Inputs:(/,-1,a," ")] [Correct Inputs: 0]
    try:
            inputs = iter(inputList)
            #Iterate through predefined inputs
            monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            #Run the game code
            import IndexGame
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Exit After New Game Fist Move Failing Test RandBulding2 took %s seconds to complete" % (time.time() - start_time))


def test_PlayGameAllChooseBuilding1(monkeypatch):
    inputList =["1",
                "1","2","3","4","5",
                "2",
                "2",
                "1",
                "1",
                "1",
                "1",
                "2",
                "1",
                "1",
                "1",
                "2",
                "2",
                "2",
                "2"]
    start_time = time.time()
    print("Beginning Play Game All Choose Random Building 1 Test")
    # Select Main Menu Option (1)
    # Choose Building Pool [Correct Inputs:(1,2,3,4,5)]
    # Choose Grid Size X-Axis [Correct Input:(2)]
    # Choose Grid Size Y-Axis [Correct Input:(2)]
    # Choose Place Random Building 1 [Correct Input: 1]
    # Choose X axis for building [Correct Input: 1]
    # Choose Y axis for building [Correct Input: 1]
    # Choose Place Random Building 1 [Correct Input: 1]
    # Choose X axis for building [Correct Input: 2]
    # Choose Y axis for building [Correct Input: 1]
    # Choose Place Random Building 1 [Correct Input: 1]
    # Choose X axis for building [Correct Input: 1]
    # Choose Y axis for building [Correct Input: 2]
    # Choose Place Random Building 1 [Correct Input: 1]
    # Choose X axis for building [Correct Input: 2]
    # Choose Y axis for building [Correct Input: 2]
    # Exit Program [Correct Input: 0]
    try:
        inputs = iter(inputList)
        #Iterate through predefined inputs
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        #Run the game code
        import IndexGame
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Play Game Always Choose Random Building 1 Test took %s seconds to complete" % (time.time() - start_time))

def test_PlayGameAllChooseBuilding2(monkeypatch):
    inputList =["1",
                "1","2","3","4","5",
                "2",
                "2",
                "2",
                "1",
                "1",
                "2",
                "2",
                "1",
                "2",
                "1",
                "2",
                "2",
                "2",
                "2"]
    start_time = time.time()
    print("Beginning Play Game All Choose Random Building 2 Test")
    # Select Main Menu Option (1)
    # Choose Building Pool [Correct Inputs:(1,2,3,4,5)]
    # Choose Grid Size X-Axis [Correct Input:(2)]
    # Choose Grid Size Y-Axis [Correct Input:(2)]
    # Choose Place Random Building 2 [Correct Input: 2]
    # Choose X axis for building [Correct Input: 1]
    # Choose Y axis for building [Correct Input: 1]
    # Choose Place Random Building 2 [Correct Input: 2]
    # Choose X axis for building [Correct Input: 2]
    # Choose Y axis for building [Correct Input: 1]
    # Choose Place Random Building 2 [Correct Input: 2]
    # Choose X axis for building [Correct Input: 1]
    # Choose Y axis for building [Correct Input: 2]
    # Choose Place Random Building 2 [Correct Input: 2]
    # Choose X axis for building [Correct Input: 2]
    # Choose Y axis for building [Correct Input: 2]
    # Exit Program [Correct Input: 0]
    try:
        inputs = iter(inputList)
        #Iterate through predefined inputs
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        #Run the game code
        import IndexGame
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Play Game Always Choose Random Building 2 Test took %s seconds to complete" % (time.time() - start_time))

def test_ExitAfterLoadGame_Pass(monkeypatch):
    inputList = ["2",
                "2",
                "0",
                "0"]
    start_time = time.time()
    print("Beginning Exit After Loaded Gamefile Test")
    # Select Main Menu Option (2)
    # Exit to Main Menu [Correct Input: 0]
    # Exit Program [Correct Input: 0]
    try:
        inputs = iter(inputList)
        #Iterate through predefined inputs
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        #Run the game code
        import IndexGame
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Exit After Load Gamefile Test took %s seconds to complete" % (time.time() - start_time))

def test_LoadGameAfterLoadGame(monkeypatch):
    inputList = ["2",
                "2",
                "0",
                "2"]
    start_time = time.time()
    print("Beginning Reload loaded gamefile after exiting loaded game Test")
    # Select Main Menu Option (2) -> Load Game
    # Exit to Main Menu (0)
    # Select Main Menu Option (2) -> Load Game
    try:
        inputs = iter(inputList)
        #Iterate through predefined inputs
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        #Run the game code
        import IndexGame
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Reload loaded gamefile after exiting loaded game Test took %s seconds to complete" % (time.time() - start_time))



def test_SaveNewGameAndLoadGame(monkeypatch):
    inputList = ["1",
                "1","2","3","4","5",
                "5",
                "5",
                "1",
                "1",
                "1",
                "2",
                "2",    
                "1",
                "3",
                "2"]
    start_time = time.time()
    print("Beginning Save New Game And Load Saved Game Test")
    # Select Main Menu Option 1 -> Start new game
    # Choose Building Pool [Correct  Inputs:(1,2,3,4,5)]
    # Choose Grid Size X-Axis [Correct Input:(5)]
    # Choose Grid Size Y-Axis [Correct Input:(5)]
    # Choose Place Random Building 1 [Correct Input: 1]
    # Choose X axis for building [Correct Input: 1]
    # Choose Y axis for building [Correct Input: 1]
    # Choose Place Random Building 2 [Correct Input: 2]
    # Choose X axis for building [Correct Input: 2]
    # Choose Y axis for building [Correct Input: 1]
    # Choose save game [Correct Input: 3]
    # Choose Main Menu Option 2 -> Load Game
    try:
            inputs = iter(inputList)
            #Iterate through predefined inputs
            monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            #Run the game code
            import IndexGame
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Load Game Saved New Game Test took %s seconds to complete" % (time.time() - start_time))

def test_SaveNewGameAndFinishLoadedGame1(monkeypatch):
    inputList = ["1",                   # Select Main Menu Option 1 -> Start new game
                "1","2","3","4","5",    # Choose Building Pool [Correct  Inputs:(1,2,3,4,5)]
                "3",                    # Choose Grid Size X-Axis [Correct Input:(5)]
                "3",                    # Choose Grid Size Y-Axis [Correct Input:(5)]
                "1",                    # Choose Place Random Building 1 [Correct Input: 1]
                "1",                    # Choose X axis for building [Correct Input: 1]
                "1",                    # Choose Y axis for building [Correct Input: 1]
                "1",                    # Choose Place Random Building 1 [Correct Input: 1]
                "2",                    # Choose X axis for building [Correct Input: 2]
                "1",                    # Choose Y axis for building [Correct Input: 1]
                "1",                    # Choose save game [Correct Input: 3]
                "3",                    # Choose Main Menu Option 2 -> Load Game
                "1",                    # Choose Place Random Building 1 [Correct Input: 1]
                "3",                    # Choose X axis for building [Correct Input: 3]
                "1",                    # Choose Y axis for building [Correct Input: 1]
                "1",                    # Choose Place Random Building 1 [Correct Input: 1]
                "1",                     # Choose X axis for building [Correct Input: 1]
                "2",                    # Choose Y axis for building [Correct Input: 2]
                "1",                    # Choose Place Random Building 1 [Correct Input: 1]
                "2",                    # Choose X axis for building [Correct Input: 2]
                "2",                    # Choose Y axis for building [Correct Input: 2]
                "1",                    # Choose Place Random Building 1 [Correct Input: 1]
                "3",                    # Choose X axis for building [Correct Input: 3]
                "2",                    # Choose Y axis for building [Correct Input: 2]
                "1",                    # Choose Place Random Building 1 [Correct Input: 1]
                "1",                    # Choose X axis for building [Correct Input: 1]
                "3",                    # Choose Y axis for building [Correct Input: 3]
                "1",                    # Choose Place Random Building 1 [Correct Input: 1]
                "2",                    # Choose X axis for building [Correct Input: 2]
                "3",                    # Choose Y axis for building [Correct Input: 3]
                "1",                    # Choose Place Random Building 1 [Correct Input: 1]
                "3",                    # Choose X axis for building [Correct Input: 3]
                "3",                    # Choose Y axis for building [Correct Input: 3]
                ]                    
    start_time = time.time()
    print("Beginning Save New Game And Load Saved Game Test")    
    try:
            inputs = iter(inputList)
            #Iterate through predefined inputs
            monkeypatch.setattr('builtins.input', lambda _: next(inputs))
            #Run the game code
            import IndexGame
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Finish Load Saved New Gamefile Test took %s seconds to complete" % (time.time() - start_time))


