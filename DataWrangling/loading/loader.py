import pandas as pd
import mariadb
from mariadb.constants import *
from pathlib import Path

# import os
# import sys

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class Loader:
    def __init__(self, data: pd.DataFrame):
        self.data: pd.DataFrame = data
        self.tupled_data: list[tuple] = self._convert_to_tuples()

    def _convert_to_tuples(self) -> list[tuple]:
        dataframe: pd.DataFrame = self.data
        dataframe = dataframe.fillna(INDICATOR.DEFAULT, inplace=True)
        dataframe_to_tuple: list[tuple] = list(
            self.data.itertuples(index=False, name=None)
        )
        return dataframe_to_tuple


class Insert:
    def __init__(
        self,
        raw_data: list[tuple],
        table_name: str,
        conn_params: dict,
        create_table_script: str | list[str],
        column_names: list[str],
    ):
        self.raw_data: list[tuple] = raw_data
        self.table_name: str = table_name
        self.conn_params: dict = conn_params
        self.column_names: list[str] = column_names
        self.columns = ", ".join(self.column_names)
        self.values = ", ".join(["?" for name in self.column_names])
        self.sql = (
            f"""INSERT INTO {self.table_name} ({self.columns}) VALUES ({self.values})"""
        )

    # Will need to be made outside, unless we have a templating engine to call?
    def _make_table(self):
        pass

    def _make_connection(self):
        try:
            return self.mariadb.connection(**self.conn_params)
        except mariadb.Error as e:
            return e

    def insert_data(self) -> None:
        with _make_connection() as con:
            cursor = connection.cursor()
            cursor.exectute_many(self.sql, self.raw_data)
            con.commit()
            cursor.close()
            con.close()
