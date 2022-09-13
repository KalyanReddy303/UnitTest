import pytest
@pytest.fixture
def one():
    return "a"
@pytest.fixture
def two():
    return []

def test_oneplustwo(one,two):
    return two.append(one)
    assert two==["a"]

