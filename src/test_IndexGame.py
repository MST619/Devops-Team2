import IndexGame
import pytest

def test_Game_calculateScore():
    result = IndexGame.buildGameList([2,2])
    expectedResult = [[' ', ' '], [' ', ' ']]