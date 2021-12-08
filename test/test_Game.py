from src import Game
import pytest

def test_Game_calculateScore():
        result = Game.calculateScore()
        assert result == ""


def test_Game_userInput():
        Game.input = lambda: "HELLO"
        # Call the function you would like to test (which uses input)
        output = Game.userInput()  
        assert output == "HELLO"
    
@pytest.mark.parametrize("input, expectedResult",
[("A1", True), ("A2", True), ("A3", True), ("A4", True),
("B1", True), ("B2", True), ("B3", True), ("B4", True),
("C1", True), ("C2", True), ("C3", True), ("C4", True),
("D1", True), ("D2", True), ("D3", True), ("D4", True),
("E1", False), ("E2", False), ("E3", False), ("E4", False),
])

def test_Game_inputLocationValidation(input, expectedResult):
        result = Game.inputLocationValidation(input)
        assert result == expectedResult

@pytest.mark.parametrize("input, expectedResult",
[("A", 0), ("A", 0), ("A", 0), ("A", 0),
("B", 1), ("B", 1), ("B", 1), ("B", 1),
("C", 2), ("C", 2), ("C", 2), ("C", 2),
("D", 3), ("D", 3), ("D", 3), ("D", 3),
("E", None), ("E", None), ("E", None), ("E", None),
])

def test_Game_inputLocationValidation(input, expectedResult):
        result = Game.checkLocList(input)
        assert result == expectedResult


def test_Game_inputLocationValidation():
        GameMap = [['','','',''],\
        ['','','',''],\
        ['','','',''],\
        ['','','','']]
        result = Game.checkValidInput(GameMap, [0,0])
        assert result == False

def test_Game_checkBuildingLeft():
        buildings = [['HSE',8],['FAC',8],['SHP',8],['HWY',8],['BCH',8]]
        PossibleOutcome = [1,2,3,4]
        result = Game.checkBuildingLeft(buildings)
        assert result in PossibleOutcome