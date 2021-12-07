import pytest
import Index

def test_Index():
    result = Index.menu()
    assert result == "helloworld"

# @pytest.mark.parametrize()

# def test_Index_menu():
#     result = exit
#     assert result == 