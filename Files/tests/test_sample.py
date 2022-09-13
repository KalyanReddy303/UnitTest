import pytest

from Files.codes.sample import add
def test_sample1():
    assert add(6,7)==13
def test_sample2():
    assert add("a","b")=="ab"
def test_sample3():
    assert add([1],[2])==[1,2]
@pytest.mark.parametrize("a,b,c",[(4,5,10),("a","b","ab"),([1],[2],[1,2])])
def test_all(a,b,c):
    assert add(a,b)==c