import pytest

from Files.codes.Sample2 import Validate_age
def test_Validation_age():
    Validate_age(10)

def test_Validation_age2():
    with pytest.raises(ValueError):
        Validate_age(-1)