
import sys
print(sys.path)

from src.code1 import add, subs

def test_add():
    print("Testing add function...")
    assert add(1, 2) == 3

def test_subs():
    print("Testing subs function...")
    assert subs(1, 2) == -1  
