import pytest

# def add(x,y):
#     return x+y

# def test1():
#     assert 2 == add(1,1)

# def test2():
#     assert 1 != add(1,1)

def func(x):
    if x == 0:
        raise ValueError("value error!")
    
    else:
        pass

def test_mytest1():
    with pytest.raises(ValueError):
        func(0)
def test_mytest2():
    assert func(1) == None