import pytest
import IndexGame
import pytest

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
=======
import IndexGame
import pytest

def test_buildingGameList():
    result = IndexGame.buildGameList([2,2])
    expectedResult = [[' ', ' '], [' ', ' ']]

    assert result == expectedResult