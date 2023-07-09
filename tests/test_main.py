import sys
sys.path.append('..')
import src.main as main

def test_calculate_total_amount(monkeypatch):
    assert main.calculate_total_amount(100, 9, 4) == 141.15816100000004