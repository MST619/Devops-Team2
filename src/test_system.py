from os import error
import pytest
import time

def test_MainMenu():
    return

#======================================== START OF BUILDING POOL TEST ====================================
def test_Game_BuildingPool_Pass_1(monkeypatch):
    start_time = time.time()
    # Select Main Menu Option (1) -> Choose Grid Size (5,5) -> Choose Building Pool (1,2,3,4,5)
    inputList = ["1","1","2","3","4","5"]
    # Iterates through the list of options that mimics user input
    print("Beginning Passing Game Pool Test 1...")
    try:
        inputs = iter(inputList)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        import IndexGame
        #Run the game code

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Building Pool Passing Test 1 took %s seconds to complete" % (time.time() - start_time))

def test_Game_BuildingPool_Pass_2(monkeypatch):
    start_time = time.time()
    # Select Main Menu Option (1) -> Choose Grid Size (5,5) -> Choose Building Pool (7,6,5,4,3)
    inputList = ["1","7","6","5","4","3"]
    # Iterates through the list of options that mimics user input
    print("Beginning Passing Game Pool Test 1...")
    try:
        inputs = iter(inputList)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        import IndexGame
        #Run the game code

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Building Pool Passing Test 2 took %s seconds to complete" (time.time() - start_time))

def test_Game_BuildingPool_Fail_1(monkeypatch):
    start_time = time.time()
    # Select Main Menu Option (1) -> Choose Building Pool (1,1,1)
    inputList = ["1","1","1"]
    # Iterates through the list of options that mimics user input
    print("Beginning Failing Game Pool Test 1...")
    try:
        inputs = iter(inputList)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        import IndexGame
        #Run the game code

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Building Pool Failing Test 1 took %s seconds to complete" (time.time() - start_time))

def test_Game_BuildingPool_Fail_2(monkeypatch):
    start_time = time.time()
    # Select Main Menu Option (1) -> Choose Building Pool (1,1,-1)
    inputList = ["1","1","-1"]
    # Iterates through the list of options that mimics user input
    print("Beginning Failing Game Pool Test 2...")
    try:
        inputs = iter(inputList)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        import IndexGame
        #Run the game code

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Building Pool Failing Test 2 took %s seconds to complete" (time.time() - start_time))

def test_Game_BuildingPool_Fail_3(monkeypatch):
    start_time = time.time()
    # Select Main Menu Option (1) -> Choose Building Pool (1,1,/)
    inputList = ["1","1","/"]
    # Iterates through the list of options that mimics user input
    print("Beginning Failing Game Pool Test 3...")
    try:
        inputs = iter(inputList)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        import IndexGame
        #Run the game code

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Building Pool Failing Test 3 took %s seconds to complete" (time.time() - start_time))

def test_Game_BuildingPool_Fail_4(monkeypatch):
    start_time = time.time()
    # Select Main Menu Option (1) -> Choose Building Pool (1,1,a)
    inputList = ["1","1","a"]
    # Iterates through the list of options that mimics user input
    print("Beginning Failing Game Pool Test 4...")
    try:
        inputs = iter(inputList)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        import IndexGame
        #Run the game code

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Building Pool Failing Test 4 took %s seconds to complete" (time.time() - start_time))

def test_Game_BuildingPool_Fail_5(monkeypatch):
    start_time = time.time()
    # Select Main Menu Option (1) -> Choose Building Pool (1,1,(space))
    inputList = ["1","1"," "]
    # Iterates through the list of options that mimics user input
    print("Beginning Failing Game Pool Test 5...")
    try:
        inputs = iter(inputList)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        import IndexGame
        #Run the game code

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Building Pool Failing Test 5 took %s seconds to complete" (time.time() - start_time))

#========================================= END OF BUILDING POOL TEST ====================================

#========================================= START OF GAME AXIS TEST ======================================
def test_Game_GameAxis_Pass_1(monkeypatch):
    start_time = time.time()
    # Select Main Menu Option (1) -> Choose Building Pool (1,2,3,4,5) -> Choose Grid Size (5,5) 
    inputList = ["1","1","2","3","4","5","5","5"]
    # Iterates through the list of options that mimics user input
    print("Beginning Passing Game Axis Test 1...")
    try:
        inputs = iter(inputList)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        import IndexGame
        #Run the game code

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        print("Finished Mocking Inputs!")
        pass
    print("Building Game Axis Passing Test 1 took %s seconds to complete" % (time.time() - start_time))

def test_startGame_Pass(monkeypatch, capfd):
    start_time = time.time()
    # Select Main Menu Option (1) -> Choose Grid Size (5,5) -> Choose Building Pool (1,2,7,5,4)
    inputList = ["1","5","5","1","2","7","5","4"]

    # Iterates through the list of options that mimics user input
    try:
        inputs = iter(inputList)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        import IndexGame
        #Run the game code

    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass

    print("\n%s seconds" % (time.time() - start_time))

def test_startGame_AxisFail(monkeypatch, capfd):
    start_time = time.time()
    # Select Main Menu Option (1) -> Choose Grid Size (5,9)
    inputList = ["1","9"]
    expectedPrint = "Invalid Input, Please try again"
    # Iterates through the list of options that mimics user input
    try:
        inputs = iter(inputList)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        import IndexGame
        #Run the game code
    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass
    out, _ = capfd.readouterr()
    assert expectedPrint in out
    print("\n%s seconds" % (time.time() - start_time))

def test_startGame_BuildingPoolFail(monkeypatch, capfd):
    start_time = time.time()
    # Select Main Menu Option (1) -> Choose Grid Size (5,5)
    inputList = ["1","5","5","1","2","8"]
    expectedPrint = "Invalid Input, Please try again"
    # Iterates through the list of options that mimics user input
    try:
        inputs = iter(inputList)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        import IndexGame
        #Run the game code
    # When list runs out of options, StopIteration error will happen unless game is exited with user inputs
    except StopIteration as e:
        pass
    out, _ = capfd.readouterr()
    assert expectedPrint in out
    print("\n%s seconds" % (time.time() - start_time))