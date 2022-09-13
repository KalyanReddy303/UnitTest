import pytest

from Files.codes.sample3 import Student


@pytest.fixture
def Student1():
    return Student("kalyan",22,"male")
def test_name(Student1):

    assert Student1.name== "kalyan"
def test_age(Student1):
    assert Student1.age == 22


def test_gender(Student1):
    assert Student1.gender == "male"
