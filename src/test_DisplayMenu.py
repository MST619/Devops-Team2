import pytest
import IndexGame

def test_displayMainMenu(capfd): #Test display menu with return value of the menu display
    IndexGame.displayMainMenu()
    out, _ = capfd.readouterr()
    assert\
    ("Welcome, mayor of Simp City!\n" +
    "------------------------------\n" +
    "1. Start new game\n" +
    "2. Load saved game\n" +
    "3. Show high scores\n" +
    "0. Exit")\
    in out

def test_runMainMenu(capfd, monkeypatch): #insert monkeypatch with expected outcome
    monkeypatch.setattr('builtins.input', lambda _: "0")
    expected = "Welcome, mayor of Simp City!\n\
------------------------------\n\
1. Start new game\n\
2. Load saved game\n\
3. Show high scores\n\
0. Exit\n\
Thanks for playing!\n"
    IndexGame.runMainMenu() #main menu runs here
    out, _ = capfd.readouterr()
    assert out == expected

def test_exit(capfd): #test exit game input
    result = IndexGame.exitGame()
    assert result == "Thanks for playing!"
    
    
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

def test_MainMenuSelection(capfd,userinput, expectedprint):
    IndexGame.MainMenuSelection(userinput)
    out, _ = capfd.readouterr()
    assert expectedprint in out