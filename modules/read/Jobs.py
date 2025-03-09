import pandas as pd


def read_jobs(path):
    jobs_df = pd.read_csv(path,
                          delimiter=",",
                          names=["id", "job"],
                          header=None,
                          dtype={
                              "id": "int64",
                              "job": "object"
                          })

    return jobs_df
