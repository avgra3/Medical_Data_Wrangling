from loader import Loader, Insert
from pathlib import Path
import pandas as pd
import pytest
import mariadb

"""PREPARING TEST DATAFRAME"""


@pytest.fixture(scope="module")
def pandas_data():
    data = {
        "case_id": [x for x in range(10)],
        "charges": [x for x in range(0, 100, 10)],
    }
    df = pd.DataFrame(data)
    return df


class TestLoader:
    """IS CONVERTED TO LIST OF TUPLES"""

    def test_is_output_list_tuple(self, pandas_data):
        expected = {"outer": list, "inner": tuple}
        actual = Loader(pandas_data)
        actual_dictionary = {
            "outer": type(actual.tupled_data),
            "inner": type(actual.tupled_data[0]),
        }
        assert expected["outer"] == actual_dictionary["outer"]
        assert expected["inner"] == actual_dictionary["inner"]


class TestInsert:
    """MAKE CONNECTION"""

    """INSERT DATA"""
