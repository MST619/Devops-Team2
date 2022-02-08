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
@pytest.mark.parametrize('map, bchscore, expected', [([['BCH', 'BCH'],[' ', ' ']], [], 6),
                                            ([['BCH', 'BCH'], ['BCH', ' ']], [], 9),
                                            ([['BCH', 'BCH', ' '], ['BCH', ' ', ' ']], [], 7),
                                            ([['BCH', 'BCH', ' '], ['BCH', ' ', 'BCH'], [' ', 'BCH', ' ']], [], 11)])
def test_bchcalc(map, bchscore, expected):
    result = IndexGame.bchcalc(map, bchscore)
    assert result == expected

@pytest.mark.parametrize('map, facscore, expected', [([['FAC', 'FAC'],[' ', ' ']], [], 4),
                                            ([['FAC', 'FAC'], ['FAC', ' ']], [], 9),
                                            ([['FAC', 'FAC', ' '], ['FAC', ' ', ' ']], [], 9),
                                            ([['FAC', 'FAC', ' '], ['FAC', ' ', 'FAC'], [' ', 'FAC', ' ']], [], 17)])
def test_faccalc(map, facscore, expected):
    result = IndexGame.faccalc(map, facscore)
    assert result == expected

@pytest.mark.parametrize('map, hsescore, expected', [([['HSE', 'FAC'],['HSE', 'BCH']], [], 4),
                                            ([['HSE', 'SHP'], ['BCH', ' ']], [], 3),
                                            ([['HSE', 'HSE', 'BCH'], ['FAC', 'SHP', 'BCH']], [], 5),
                                            ([['HSE', ' ', 'BCH'], ['FAC', 'SHP', 'HSE'], ['BCH', 'HSE', 'HWY']], [], 7)])
def test_hsecalc(map, hsescore, expected):
    result = IndexGame.hsecalc(map, hsescore)
    assert result == expected

@pytest.mark.parametrize('map, shpscore, expected', [([['SHP', 'SHP'],['FAC', 'HSE']], [], 4),
                                            ([['SHP', 'FAC'], ['FAC', ' ']], [], 1),
                                            ([['SHP', 'FAC', ' '], ['BCH', 'SHP', 'HSE']], [], 5),
                                            ([['FAC', 'HSE', ' '], ['BCH', 'SHP', 'HWY'], [' ', 'FAC', ' ']], [], 4)])
def test_shpcalc(map, shpscore, expected):
    result = IndexGame.faccalc(map, shpscore)
    assert result == expected

@pytest.mark.parametrize('map, hwyscore, expected', [([['HWY', 'HWY'],['FAC', 'HSE']], [], 4),
                                            ([['HWY', 'FAC'], ['FAC', ' ']], [], 1),
                                            ([['HWY', 'HWY', ' '], ['HWY', 'HWY', 'HWY']], [], 13),
                                            ([['FAC', 'HSE', 'HWY'], ['HWY', 'WY', 'HWY'], ['HWY', 'HWY', ' ']], [], 14)])
def test_hwycalc(map, hwyscore, expected):
    result = IndexGame.hwycalc(map, hwyscore)
    assert result == expected

@pytest.mark.parametrize('map, prkscore, expected', [([['PRK', 'PRK'],['FAC', 'HSE']], [], 2),
                                            ([['PRK', 'FAC'], ['PRK', 'PRK']], [], 8),
                                            ([['PRK', 'PRK', 'PRK'], ['HWY', 'PRK', 'PRK']], [], 22),
                                            ([['PRK', 'HSE', 'PRK'], ['PRK', 'PRK', 'PRK'], ['PRK', 'HWY', 'PRK']], [], 24)])
def test_prkcalc(map, prkscore, expected):
    result = IndexGame.prkcalc(map, prkscore)
    assert result == expected

@pytest.mark.parametrize('map, monscore, expected', [([['MON', 'MON'],['MON', 'MON']], [], 16),
                                            ([['MON', 'MON'], ['FAC', ' ']], [], 4),
                                            ([['MON', 'MON', ' '], ['MON', 'HWY', 'HWY']], [], 5),
                                            ([['MON', 'HSE', 'MON'], ['HWY', 'MON', 'HWY'], ['MON', 'MON', ' ']], [], 20), 
                                            ([['MON', 'HSE', 'MON'], ['MON', 'HWY', 'HWY'], ['MON', 'HSE', ' ']], [], 16)])
def test_moncalc(map, monscore, expected):
    result = IndexGame.moncalc(map, monscore)
    assert result == expected


def test_displayscore():
    result = IndexGame.displayScore()
    expectedResult = False
    assert result == expectedResult