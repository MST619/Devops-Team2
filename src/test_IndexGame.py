import IndexGame
import pytest
import module

def test_buildingGameList():
    result = IndexGame.buildGameList([2,2])
    expectedResult = [[' ', ' '], [' ', ' ']]

    assert result == expectedResult

def test_defineGameMapSize(self):
    module.input = lambda: '1'
    module.input = lambda: '2'
    result = IndexGame.buildGameMap()
    assert result == [1,2]

