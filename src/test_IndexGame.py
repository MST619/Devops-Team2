import IndexGame
import pytest
from unittest.mock import Mock, patch
from gameinit import buildingPool

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
                "BCH":8, 
                "HSE":8,
                "SHP":8,
                "FAC":8,
                "HWY":0,
                "MON":8,
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

#4.1.1
def test_remainingBuildings():
    result = IndexGame.remainingBuildings()
    expectedResult = { 
                "BCH":8, 
                "HSE":8,
                "SHP":8,
                "FAC":8,
                "HWY":0,
                "MON":8,
                "PRK":0
            }
    assert result == expectedResult

#4.4 
@pytest.mark.parametrize('map, bchscore, expected', [([['BCH', 'BCH'],[' ', ' ']], 0, 6),
                                            ([['BCH', 'BCH'], ['BCH', ' ']], 0, 9),
                                            ([['BCH', 'BCH', ' '], ['BCH', ' ', ' ']], 0, 7),
                                            ([['BCH', 'BCH', ' '], ['BCH', ' ', 'BCH'], [' ', 'BCH', ' ']], 0, 11)])
def test_bchcalc(map, bchscore, expected):
    result = IndexGame.bchcalc(map, bchscore)
    assert result == expected

def test_faccalc():
    result = IndexGame.faccalc([['FAC', 'FAC'], [' ', ' ']], 0)
    expected = 4
    assert result == expected

def test_displayscore():
    result = IndexGame.displayScore()
    expectedResult = False
    assert result == expectedResult