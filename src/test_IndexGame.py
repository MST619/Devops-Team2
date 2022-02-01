import IndexGame
import pytest
from unittest.mock import Mock, patch


#def test_displayMainMenu(capfd): #Test display menu with return value of the menu display
#    IndexGame.displayMainMenu()
#    out, _ = capfd.readouterr()
#    assert\
#    ("Welcome, mayor of Simp City!\n" +
#    "------------------------------\n" +
#    "1. Start new game\n" +
#    "2. Load saved game\n" +
#    "3. Show high scores\n" +
#    "0. Exit")\
#    in out

#def test_runMainMenu(capfd, monkeypatch): #insert monkeypatch with expected outcome
#    monkeypatch.setattr('builtins.input', lambda _: "0")
#    expected = "Welcome, mayor of Simp City!\n\
#------------------------------\n\
#1. Start new game\n\
#2. Load saved game\n\
#3. Show high scores\n\
#0. Exit\n\
#Thanks for playing!\n"
#    IndexGame.runMainMenu() #main menu runs here
#    out, _ = capfd.readouterr()
#    assert out == expected

#def test_exit(capfd): #test exit game input
#    result = IndexGame.exitGame()
#    assert result == "Thanks for playing!"
    
    
@pytest.mark.parametrize("userinput, expectedprint",
                        [("0","Thanks for playing!"),
                        ("1",
                        "Turn 1\n" + 
                        "    A     B     C     D\n"+
                        " " + "+-----+-----+-----+-----+\n" +
                        "1|     |     |     |     |\n" +
                        " " + "+-----+-----+-----+-----+\n" +
                        "2|     |     |     |     |\n" +
                        " " + "+-----+-----+-----+-----+\n" +
                        "3|     |     |     |     |\n" +
                        " " + "+-----+-----+-----+-----+\n" +
                        "4|     |     |     |     |\n" +
                        " " + "+-----+-----+-----+-----+\n" +
                        "Feature still in development!\n"),
                        ("2","Load a save file"),
                        ("3","Display Leaderboard"),
                        ("a", "Invalid input!"),
                        ("/", "Invalid input!"),
                        (22, "Invalid input!"),
                        (-1, "Invalid input!")])

def test_MainMenuSelection(userinput, expectedprint): #add capfd back when testing display
    IndexGame.MainMenuSelection(userinput)
    #out, _ = capfd.readouterr()
    assert expectedprint

#2.1
input_mock_1 = Mock()
input_mock_1.return_value = "HSE"
input_mock_2 = Mock()
input_mock_2.return_value = "FAC"
input_mock_3 = Mock()
input_mock_3.return_value = "SHP"
input_mock_4 = Mock()
input_mock_4.return_value = "BCH"
input_mock_5 = Mock()
input_mock_5.return_value = "MON"

input_mock = Mock()
input_mock.side_effect = [input_mock_1.return_value, input_mock_2.return_value, input_mock_3.return_value, input_mock_4.return_value, input_mock_5.return_value]
def test_chooseBuildingPool():
    with patch('builtins.input', input_mock) as mock_method:
        result = IndexGame.chooseBuildingPool()
    expected = { 
                "BCH":5, 
                "HSE":5,
                "SHP":5,
                "FAC":5,
                "HWY":0,
                "MON":5,
                "PRK":0
            }
    assert mock_method.call_count == 5
    assert result == expected
#2.2.2
def test_buildingGameList():
    result = IndexGame.buildGameList([2,2])
    expectedResult = [[' ', ' '], [' ', ' ']]

    assert result == expectedResult

#3.1
def test_CheckFile():
    result =  IndexGame.checkFile("LoadGame")
    expectedResult = False

    assert result == expectedResult

#3.2
def test_LoadGame():
    result = IndexGame.loadGame()
    expectedResult = False

    assert result == expectedResult
