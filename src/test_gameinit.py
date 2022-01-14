import pytest
import gameinit
from unittest.mock import Mock, patch

@pytest.mark.parametrize("xAxis, yAxis, expectedreturn",
    [(2, 3, [['     A     B   '], ['  +-----+-----+'], [' ', '1', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ''], ['  +-----+-----+'], [' ', '2', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 
' ', '|', ''], ['  +-----+-----+'], [' ', '3', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ''], ['  +-----+-----+']])])
def test_gameGrid(xAxis, yAxis, expectedreturn):
    result = gameinit.gameGrid(xAxis, yAxis)
    assert result == expectedreturn



input_mock_x = Mock()
input_mock_x.return_value = 4
input_mock_y = Mock()
input_mock_y.return_value = 3

input_mock = Mock()
input_mock.side_effect = [input_mock_x.return_value, input_mock_y.return_value]


def test_newGame():
    with patch('builtins.input', input_mock) as mock_method:
        result = gameinit.newGame()

    assert mock_method.call_count == 2
    assert result == (4, 3)