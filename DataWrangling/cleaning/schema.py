import pandera as pa
import pandas as pd


# Required columns
def validator(df: pd.DataFrame) -> pd.DataFrame:
    required_columns = pa.DataFrameSchema(
        {
            "case_id": pa.Column(
                pd.Int64Dtype(), pa.Check.greater_than_or_equal_to(0), required=True
            ),
            "attd_physician_code": pa.Column(
                pd.Int64Dtype(), pa.Check.equal_to(1), required=True
            ),
            "oper_physician_code": pa.Column(
                pd.Int64Dtype(), pa.Check.equal_to(1), required=True
            ),
            "hospital_code": pa.Column(
                pd.Int64Dtype(), pa.Check.equal_to(0), required=True
            ),
            "period_code": pa.Column(
                pd.Int64Dtype(), pa.Check.equal_to(1900), required=True
            ),
            "los": pa.Column(pd.Int64Dtype(), pa.Check.equal_to(9999), required=True),
            "charge": pa.Column(pd.Float64Dtype, pa.Check.equal_to(0.0), required=True),
            "gender_code": pa.Column(
                pd.StringDtype(), pa.Check.str_matches("X"), required=True
            ),
            "ethnicity_code": pa.Column(
                pd.Int64Dtype(), pa.Check.equal_to(0), required=True
            ),
            "age_code": pa.Column(
                pd.Int64Dtype(), pa.Check.equal_to(999), required=True
            ),
            "zip_code": pa.Column(
                pd.StringDtype(), pa.Check.str_matches("XXXXX"), required=True
            ),
            "st_payor_code": pa.Column(
                pd.StringDtype(), pa.Check.str_matches("XXX"), required=True
            ),
            "ins_carrier_code": pa.Column(
                pd.StringDtype(), pa.Check.str_matches("0"), required=True
            ),
            "drg_code": pa.Column(
                pd.StringDtype(), pa.Check.str_matches("470"), required=True
            ),
            "aprdrg_code": pa.Column(
                pd.StringDtype(), pa.Check.str_matches("9999"), required=True
            ),
            "discharge_status_code": pa.Column(
                pd.Int64Dtype(), pa.Check.equal_to(0), required=True
            ),
            "admission_type_code": pa.Column(
                pd.Int64Dtype(), pa.Check.equal_to(998), required=True
            ),
            "admission_date": pa.Column("datetime64[ns]", required=True),
            "discharge_date": pa.Column("datetime64[ns]", required=True),
            "admission_src_code": pa.Column(
                pd.Int64Dtype(), pa.Check.equal_to(999), required=True
            ),
            "diagnosis_code": pa.Column(
                pd.StringDtype(), pa.Check.equal_to(pd.NA), nullable=True, required=True
            ),
            "procd_code": pa.Column(
                pd.StringDtype(), pa.Check.equal_to(pd.NA), nullable=True, required=True
            ),
            "complication_code": pa.Column(
                pd.Int64Dtype(), pa.Check.equal_to(0), required=True
            ),
            "bac_code": pa.Column(pd.Int64Dtype(), pa.Check.equal_to(0), required=True),
            "mort_code": pa.Column(
                pd.Int64Dtype(), pa.Check.equal_to(0), required=True
            ),
            "merge_code": pa.Column(
                pd.StringDtype(), pa.Check.str_matches("y"), required=True
            ),
            "bed_type_code": pa.Column(
                pd.StringDtype(), pa.Check.str_matches("0"), required=True
            ),
            "drg_outlier_code": pa.Column(
                pd.StringDtype(), pa.Check.str_matches("IN"), required=True
            ),
            "drg_outlier": pa.Column(
                pd.Int64Dtype(), pa.Check.equal_to(0), required=True
            ),
            "msdrg_code": pa.Column(
                pd.StringDtype(), pa.Check.equal_to(pd.NA), required=True, nullable=True
            ),
        },
        strict="filter",
    )
    return required_columns.validate(df)
