from os import error
import pytest
import time
import test_system as ts

def test_ExitAfterGameSetup_Pass1_benchmark(benchmark,monkeypatch):
    benchmark.pedantic(ts.test_ExitAfterGameSetup_Pass1(monkeypatch), rounds=100)