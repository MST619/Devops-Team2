import pytest
import Index2

def test_displayMainMenu(capfd):
    Index2.displayMainMenu()
    out, _ = capfd.readouterr()
    assert\
    """Welcome, mayor of Simp City!\n------------------------------\n1. Start new game\n2. Load saved game\n3. Show high scores\n0. Exit"""\
    in out

def test_exit(capfd):
    Index2.exitGame()
    out, _ = capfd.readouterr()
    assert\
        """Thanks for playing!"""

# @pytest.mark.parametrize("input",("0"))
# def test_MainMenuSelection(capfd,input):
#     Index2.MainMenuSelection(input)
#     out, _ = capfd.readouterr()
#     assert\
#         """Thanks for playing!"""
    

def test_MainMenuSelection(capfd,monkeypatch):
    input = 0
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda x: input)
    Index2.MainMenuSelection(input)
    out, _ = capfd.readouterr()
    assert\
        """Thanks for playing!"""
