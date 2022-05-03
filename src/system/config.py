import pathlib


CSV_DELIMITER = ";"


ABS_ROOT_PATH = pathlib.Path(__file__).resolve().parents[2]

EMPLOYEE_LIST_PATH = ABS_ROOT_PATH.joinpath("employees.csv")

