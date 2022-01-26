import IndexGame
import pytest

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