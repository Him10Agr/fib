import os
import pathlib
from typing import Tuple, List, Union
import requests

def get_latest_version_number() -> str:

    req = requests.get(
        "https://pypi.org/pypi/fib_him10agr.py/json"
    )

    return req.json()["info"]["version"]

def unpack_version_number(version_string: str) -> Tuple(int, int, int):

    version_buffer: List[str] = version_string.split(".")
    return (version_string[i] for i in range(len(version_buffer)))

def increase_version_number(version_buffer: Union[Tuple[int, int, int], List[int]]) -> List[int]:

    first: int = version_buffer[0]
    second: int = version_buffer[1]
    third: int = version_buffer[2]
    third += 1
    if third >= 10:
        third = 0
        second += 1
        if second >= 10:
            second = 0
            first += 1

def pack_version_number(version_buffer: Union[Tuple[int, int, int], List[int]]) -> str:

    return f"{version_buffer[0]}.{version_buffer[1]}.{version_buffer[2]}"

def write_version_to_file(version_number: str) -> None:

    version_file_path: str = str(pathlib.Path(__file__).parent.absolute()) + "/fib/version.py"

    if os.path.exists(version_file_path):
        os.remove(version_file_path)
    with open(version_file_path, "w") as f:
        f.write(f"VERSION='{version_number}'")


if __name__ == "__main__":

    write_version_to_file(
        version_number=pack_version_number(
            version_buffer=increase_version_number(
                version_buffer=unpack_version_number(
                    version_string=get_latest_version_number()
                )
            )
        )
    )