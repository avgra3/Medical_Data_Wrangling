from cleaning.cleaner import RawData
from pathlib import Path
from raw_test.data_types import oral_ip_main


raw_path = Path("./raw_test/Orip4qtr22.txt")

new_raw = RawData(oral_ip_main, raw_location=raw_path, file_type="csv", delim="|")

if __name__ == "__main__":
    if raw_path.exists() and raw_path.is_file():
        new_raw.cleaned.head()
    else:
        print(f"File does not exist at {raw_path.resolve()}")
