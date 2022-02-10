from pickle import FALSE
from unittest import mock
from _pytest.monkeypatch import monkeypatch
import IndexGame
import pytest
from unittest.mock import Mock, patch




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
@pytest.mark.parametrize("inputList, expected", [([2,2], [[' ', ' '], [' ', ' ']]), 
                        ([3,4], [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]),
                        ([5,5], [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']])])
def test_passingbuildingGameList(inputList, expected):
    result = IndexGame.buildGameList(inputList)
    assert result == expected

# @pytest.mark.parametrize("inputList, expected", [([-2,2], "Invalid map size, please keep within 40 spaces"), 
#                         ([20,4], "Invalid map size, please keep within 40 spaces"),
#                         ([300,1], "Invalid map size, please keep within 40 spaces")])
# def test_failingbuildingGameList(capfd, inputList, expected):
#     IndexGame.buildGameList(inputList)
#     out, _ = capfd.readouterr()
#     assert expected in out

# # 3.1
# def test_CheckFile():
#     result =  IndexGame.checkFile("LoadGame")
#     expectedResult = False

#     assert result == expectedResult

# # 3.2
# def test_LoadGame():
#     result = IndexGame.loadGame()
#     expectedResult = False

#     assert result == expectedResult

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


#4.2.2
map = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
@pytest.mark.parametrize("map, input, expected", [(map, "A1", True), (map, "A2", True),
                        (map, "C3", True), (map, "B2", True)])
def test_passingpositionCheck(map, input, expected):
    result = IndexGame.positionCheck(map, input)
    assert result == expected


@pytest.mark.parametrize("map, input, expected", [(map, "C4", False), (map, "H6", False),
                        (map, "D3", False), (map, "N8", False)])
def test_failingpositionCheck(map, input, expected):
    result = IndexGame.positionCheck(map, input)
    assert result == expected

map1 = [[' ', ' ', ' '],[' ', 'BCH', ' '],[' ', ' ', ' ']]

@pytest.mark.parametrize("map1, row, column, expected", [(map1, 1, "A", True), (map1, 2, "A", True)])
def test_passingemptyCheck(map1, row, column, expected):
    result = IndexGame.emptyCheck(map1, row, column)
    assert result == expected

@pytest.mark.parametrize("map1, row, column, expected", [(map1, 2, "B", False)])
def test_failingemptyCheck(map1, row, column, expected):
    result = IndexGame.emptyCheck(map1, row, column)
    assert result == expected

@pytest.mark.parametrize("buildingPool, selectedBuildings, expected", [({
                "BCH":8, 
                "HSE":8,
                "SHP":8,
                "FAC":8,
                "HWY":0,
                "MON":8,
                "PRK":0
            }, "BCH", { 
                "BCH":7, 
                "HSE":8,
                "SHP":8,
                "FAC":8,
                "HWY":0,
                "MON":8,
                "PRK":0
            })])
def test_deductBuildingPool(buildingPool, selectedBuildings, expected):
    result = IndexGame.deductBuildingPool(buildingPool, selectedBuildings)
    assert result == expected

@pytest.mark.parametrize("map, selectedBuilding, buildingPool, turn, input, expected", [(map, "BCH", {
                "BCH":8, 
                "HSE":8,
                "SHP":8,
                "FAC":8,
                "HWY":0,
                "MON":8,
                "PRK":0
            }, 1, "A1", [['BCH', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])])
def test_buildBuildings(map, selectedBuilding, buildingPool, turn, input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'A1')
    result = IndexGame.buildBuildings(map, selectedBuilding, buildingPool, turn, input)
    assert result == expected
    

def test_randomBuilding():
    availabletypes = ['BCH', 'HSE', 'SHP', 'FAC', 'MON']
    result = IndexGame.randomBuilding({
                "BCH":8, 
                "HSE":8,
                "SHP":8,
                "FAC":8,
                "HWY":0,
                "MON":8,
                "PRK":0
            })
    expected = "BCH", "FAC"
    if result in availabletypes:
        assert result == expected