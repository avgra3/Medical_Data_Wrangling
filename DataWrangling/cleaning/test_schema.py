from schema import validator
import pytest
from pandas import DataFrame
import pandera as pa

"""NEEDED FIXTURES"""


@pytest.fixture(scope="session")
def basic_pandas():
    data = {
        "input_case_id": [f"{x * 100}" for x in range(100)],
        "input_address": [f"{x} Random Rd" for x in range(100)],
    }
    return DataFrame(data)


@pytest.fixture(scope="session")
def valid_pandas():
    data = {
        "input_case_id": [f"{x * 100}" for x in range(100)],
        "input_address": [f"{x} Random Rd" for x in range(100)],
    }

    return DataFrame(data)


"""TESTS"""


def test_validator(basic_pandas, mocker):
    # Test if dataframe schema fails correctly
    with pytest.raises(pa.SchemaError):
        validator(basic_pandas)
