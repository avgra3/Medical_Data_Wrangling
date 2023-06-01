from cleaning.cleaner import RawData
from pathlib import Path
from decouple import config
import pandas as pd

raw_path = Path(config("DATA_PATH", cast=str))

new_raw = RawData(
    eval(config("DATA_TYPES")),
    raw_location=raw_path,
    file_type="csv",
    delim="|",
)

if __name__ == "__main__":
    if raw_path.exists() and raw_path.is_file():
        print(new_raw.cleaned.shape)
    else:
        print(f"File does not exist at {raw_path.resolve()}")
