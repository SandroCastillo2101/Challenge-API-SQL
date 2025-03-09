import pandas as pd


def read_employees(path):
    employees_df = pd.read_csv(path,
                               delimiter=",",
                               names=["id", "name", "datetime", "department_id", "job_id"],
                               header=None,
                               dtype={
                                   "id": "int64",
                                   "name": "object",
                                   "department_id": "float64",
                                   "job_id": "float64"
                               },
                               parse_dates=["datetime"])

    return employees_df
