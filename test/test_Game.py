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
    