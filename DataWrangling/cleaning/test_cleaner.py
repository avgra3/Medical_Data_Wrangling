from cleaner import RawData
from pathlib import Path
import pandas as pd
import pytest

"""CREATE NEEDED FIXTURES"""


@pytest.fixture(scope="session")
def basic_pandas():
    data = {
        "input_case_id": [f"{x * 100}" for x in range(100)],
        "input_address": [f"{x} Random Rd" for x in range(100)],
    }
    return pd.DataFrame(data)


@pytest.fixture(scope="session")
def column_type():
    col_type = {
        "input_case_id": pd.StringDtype(),
        "address": pd.StringDtype(),
    }
    return col_type


@pytest.fixture(scope="session")
def file_location(tmp_path_factory, basic_pandas):
    fake_path = tmp_path_factory.mktemp("data") / "test_load.csv"
    basic_pandas.to_csv(fake_path, sep="\n", index=False)
    return fake_path


@pytest.fixture(scope="session")
def raw_class(tmp_path_factory, basic_pandas, column_type) -> RawData:
    fake_path = tmp_path_factory.mktemp("data") / "test_load.csv"
    basic_pandas.to_csv(fake_path, sep="\n", index=False)
    return RawData(column_type, fake_path, fake_path.suffix[1:])


class TestRawData:
    added_columns: list[str] = [
        "case_id",
        "attd_physician_code",
        "oper_physician_code",
        "hospital_code",
        "period_code",
        "los",
        "charge",
        "gender_code",
        "ethnicity_code",
        "age_code",
        "zip_code",
        "st_payor_code",
        "ins_carrier_code",
        "drg_code",
        "aprdrg_code",
        "discharge_status_code",
        "admission_type_code",
        "admission_date",
        "discharge_date",
        "admission_src_code",
        "diagnosis_code",
        "procd_code",
        "complication_code",
        "bac_code",
        "mort_code",
        "merge_code",
        "bed_type_code",
        "drg_outlier_code",
        "drg_outlier",
        "msdrg_code",
    ]

    def test_raw_data_class(self, raw_class):
        assert type(raw_class) == RawData

    def test_columns_added(self, raw_class):
        assert set(self.added_columns).issubset(
            list(raw_class._add_needed_columns().columns)
        )

    def test_is_pandas(self, raw_class):
        # <class 'pandas.core.frame.DataFrame'>
        # pd.core.frame.DataFrame
        df = raw_class.cleaned
        assert isinstance(type(df), pd.DataFrame.__class__)
        # assert isinstance(df, pd.core.frame.DataFrame)
        # assert type(df) is pd.core.frame.DataFrame
