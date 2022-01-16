from os import error
import pytest
import Index


@pytest.mark.parametrize("input","GameMap","turns","x_counter","y_counter","buildingPool",
                        "game1", 
                        [['     A     B   '], ['  +-----+-----+'], [' ', '1', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ''], ['  +-----+-----+'], [' ', '2', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ''], ['  +-----+-----+']],
                        0,
                        2,
                        2,
                        buildingPool = {
                            "BCH":4, 
                            "HSE":5,
                            "SHP":5,
                            "FAC":5,
                            "HWY":5,
                            "MON":5,
                            "PRK":5
                        }
def test_getFile(capfd):