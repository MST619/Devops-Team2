import pytest
import Index2

def test_displayMainMenu(capfd):
    Index2.displayMainMenu()
    out, _ = capfd.readouterr()
    assert\
    """Welcome, mayor of Simp City!\n------------------------------\n1. Start new game\n2. Load saved game\n3. Show high scores\n0. Exit"""\
    in out

def test_exit(capfd):
    result = Index2.exitGame()
    assert result == "Thanks for playing!"

@pytest.mark.parametrize("input, expectedprint",[("0","Thanks for playing!"),("1","Feature still under development!"),("2","Feature still under development!"),("3","Feature still under development!"),("a", "Invalid input!"),("/", "Invalid input!"),(22, "Invalid input!"),(-1, "Invalid input!")])
def test_MainMenuSelection(capfd,input, expectedprint):
    Index2.MainMenuSelection(input)
    out, _ = capfd.readouterr()
    assert expectedprint in out
    

# def test_MainMenuSelection(capfd,monkeypatch):
#     input = "0"
#     # with monkeypatch.context() as m:
#     #     m.setattr('builtins.input', lambda x: input)
#     Index2.MainMenuSelection(input)
#     out, _ = capfd.readouterr()
#     assert\
#     """Thanks for playing!"""\
#     in out
#     # Test option 2
#     input = "1"
#     Index2.MainMenuSelection(input)
#     out, _ = capfd.readouterr()
#     assert\
#     """Feature still under development!"""\
#     in out
#     # Test option 2
#     input = "2"
#     Index2.MainMenuSelection(input)
#     out, _ = capfd.readouterr()
#     assert\
#     """Feature still under development!"""\
#     in out
#     # Test option 3
#     input = "3"
#     Index2.MainMenuSelection(input)
#     out, _ = capfd.readouterr()
#     assert\
#     """Feature still under development!"""\
#     in out
#     input = "invalid"
#     Index2.MainMenuSelection(input)
#     out, _ = capfd.readouterr()
#     assert\
#     """Invalid input!"""\
#     in out

