from os import error
import pytest
import scorecalc

@pytest.mark.parametrize("gameGridList, expectedScore",
        [[['     A     B     C     D     E   '], ['  +-----+-----+-----+-----+-----+'], 
        [' ', '1', '|', ' BCH ', '|', ' HSE ', '|', ' HSE ', '|', ' FAC ', '|', ' BCH ', '|'],
        ['   +-----+-----+-----+-----+-----+'],
        [' ', '2', '|', ' BCH ', '|', ' HSE ', '|', ' HSE ', '|', ' FAC ', '|', ' FAC ' '|'],
        ['   +-----+-----+-----+-----+-----+'],
        [' ', '3', '|', ' PRK ', '|', ' PRK ', '|', ' FAC' , '|', ' FAC ', '|', ' FAC ', '|'],
        ['   +-----+-----+-----+-----+-----+'],
        [' ', '4', '|', ' PRK ', '|', ' PRK ', '|', ' HSE ', '|', ' HSE ', '|', ' BCH ', '|'],
        ['   +-----+-----+-----+-----+-----+'],
        [' ', '5', '|', ' HWY ', '|', ' HWY ', '|', ' HWY ', '|', ' HWY ', '|', ' HWY ', '|']], 58])
 

def test_scorecalc(gameGridList, expectedScore):
    result = scorecalc(gameGridList)
    assert result == expectedScore
