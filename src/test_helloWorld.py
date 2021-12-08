import helloWorld
import pytest

def test_helloWorld():
    result = helloWorld.helloWorld()
    assert result == "hello"