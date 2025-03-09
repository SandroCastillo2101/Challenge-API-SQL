import pandas as pd


def read_departments(path):
    departments_df = pd.read_csv(path,
                                 delimiter=",",
                                 names=["id", "department"],
                                 header=None,
                                 dtype={
                                     "id": "int64",
                                     "department": "object"
                                 })

    return departments_df
