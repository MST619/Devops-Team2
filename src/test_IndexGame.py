import pytest
import IndexGame

#2.1
def test_chooseBuildingPool(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "BCH HSE SHP FAC MON")
    expected = { 
                "BCH":5, 
                "HSE":5,
                "SHP":5,
                "FAC":5,
                "HWY":0,
                "MON":5,
                "PRK":0
            }
    result = IndexGame.chooseBuildingPool()
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