import pandas as pd
from pathlib import Path


# Data Object
class RawData:
    def __init__(
        self,
        column_dict,
        raw_location,
        file_type,
        min_case_id: int = 0,
        delim: str = None,
        header: str | bool = False,
    ):
        self.column_dict: dict = column_dict
        self.raw_location: str | Path = raw_location
        self.file_type: str = file_type
        self.delim: str = delim
        self.min_case_id: int = min_case_id
        self.header: str | bool = header
        self.cleaned: pd.DataFrame = self._add_needed_columns()

    # Load into a dataframe
    def _load_data_frame(self) -> pd.DataFrame | None:
        if self.file_type in ["csv", "text", "txt", "tab"]:
            print("csv")
            dataframe = pd.read_csv(
                self.raw_location,
                sep=self.delim,
                parse_dates=False,
                dtype=self.column_dict,
            )
            return dataframe

        if self.file_type in ["fixed", "fw"]:
            print("Too difficult")

    # Add new columns
    def _add_needed_columns(self) -> pd.DataFrame:
        cleaned_dataframe = self._load_data_frame()
        cleaned_dataframe["case_id"]: pd.Int64() = (
            cleaned_dataframe.index + self.min_case_id + 1
        )
        cleaned_dataframe["attd_physician_code"]: pd.Int64() = 1
        cleaned_dataframe["oper_physician_code"]: pd.Int64() = 1
        cleaned_dataframe["hospital_code"]: pd.Int64() = 0
        cleaned_dataframe["period_code"]: pd.Int64() = 1900
        cleaned_dataframe["los"]: pd.Int64() = 9999
        cleaned_dataframe["charge"]: pd.Float64Dtype() = 0.0
        cleaned_dataframe["gender_code"]: pd.StringDtype() = "X"
        cleaned_dataframe["ethnicity_code"]: pd.Int64() = 0
        cleaned_dataframe["age_code"]: pd.Int64() = 999
        cleaned_dataframe["zip_code"]: pd.StringDtype() = "XXXXX"
        cleaned_dataframe["st_payor_code"]: pd.StringDtype() = "XXX"
        cleaned_dataframe["ins_carrier_code"]: pd.StringDtype() = "0"
        cleaned_dataframe["drg_code"]: pd.StringDtype() = "470"
        cleaned_dataframe["aprdrg_code"]: pd.StringDtype() = "9999"
        cleaned_dataframe["discharge_status_code"]: pd.Int64() = 0
        cleaned_dataframe["admission_type_code"]: pd.Int64() = 998
        cleaned_dataframe["admission_date"]: pd.datetime64() = "1900-01-01"
        cleaned_dataframe["discharge_date"]: pd.datetime64() = "1900-01-01"
        cleaned_dataframe["admission_src_code"]: pd.Int64() = 999
        cleaned_dataframe["diagnosis_code"]: pd.StringDtype() = pd.NA
        cleaned_dataframe["procd_code"]: pd.StringDtype() = pd.NA
        cleaned_dataframe["complication_code"]: pd.Int64() = 0
        cleaned_dataframe["bac_code"]: pd.Int64() = 0
        cleaned_dataframe["mort_code"]: pd.Int64() = 0
        cleaned_dataframe["merge_code"]: pd.StringDtype() = "y"
        cleaned_dataframe["bed_type_code"]: pd.StringDtype() = "0"
        cleaned_dataframe["drg_outlier_code"]: pd.StringDtype() = "IN"
        cleaned_dataframe["drg_outlier"]: pd.Int64() = 0
        cleaned_dataframe["msdrg_code"]: pd.StringDtype() = pd.NA

        print(cleaned_dataframe.head())
        return cleaned_dataframe
