import pytest
import Index

def test_displayMainMenu(capfd):
    Index.displayMainMenu()
    out, _ = capfd.readouterr()
    assert\
    ("Welcome, mayor of Simp City!\n" +
    "------------------------------\n" +
    "1. Start new game\n" +
    "2. Load saved game\n" +
    "3. Show high scores\n" +
    "0. Exit")\
    in out

def test_runMainMenu():
    result = 1
    while result != 0:
        assert result == Index.displayMainMenu()
        userInput = input("Enter your option: ")
        result = Index.MainMenuSelection(userInput)
        return Index.MainMenuSelection(userInput)
        
def test_exit(capfd):
    result = Index.exitGame()
    assert result == "Thanks for playing!"

@pytest.mark.parametrize("input, expectedprint",
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
                        ("2","Feature still under development!"),
                        ("3","Feature still under development!"),
                        ("a", "Invalid input!"),
                        ("/", "Invalid input!"),
                        (22, "Invalid input!"),
                        (-1, "Invalid input!")])
def test_MainMenuSelection(capfd,input, expectedprint):
    Index.MainMenuSelection(input)
    out, _ = capfd.readouterr()
    assert expectedprint in out
    

