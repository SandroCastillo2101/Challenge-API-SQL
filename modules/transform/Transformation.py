from modules.read.Departments import read_departments
from modules.read.Employees import read_employees
from modules.read.Jobs import read_jobs


def read_inputs(main_path):
    departments_df = read_departments(main_path + "/departments/departments.csv")
    departments_df.rename(columns={"id": "department_id"}, inplace=True)

    employees_df = read_employees(main_path + "/employees/hired_employees.csv")
    employees_df[["id", "department_id", "job_id"]] = employees_df[["id", "department_id", "job_id"]].fillna(0)
    employees_df = employees_df.astype({"id": "int64", "department_id": "int64", "job_id": "int64"})

    jobs_df = read_jobs(main_path + "/jobs/Jobs.csv")
    jobs_df.rename(columns={"id": "job_id"}, inplace=True)

    return departments_df, employees_df, jobs_df


def employees_by_quarter(main_path):
    departments_df, employees_df, jobs_df = read_inputs(main_path)
    employees_joined_departments_df = employees_df.merge(departments_df,
                                                         on="department_id",
                                                         how="left")
    employees_full_df = employees_joined_departments_df.merge(jobs_df,
                                                              on="job_id",
                                                              how="left")
    employees_full_df["Q"] = employees_full_df["datetime"].dt.quarter
    employees_full_df["Q"].replace({1.0: "Q1", 2.0: "Q2", 3.0: "Q3", 4.0: "Q4"}, inplace=True)
    grouped_df = employees_full_df.groupby(["department", "job", "Q"]).size().reset_index(name="number")
    result_df = grouped_df.pivot_table(index=["department", "job"], columns="Q", values="number", fill_value=0)
    result_df = result_df.reset_index()
    result_df = result_df.sort_values(by=["department", "job"], ascending=[True, True])
    return result_df


def hired_employees_by_department(main_path):
    departments_df, employees_df, jobs_df = read_inputs(main_path)
    employees_joined_departments_df = employees_df.merge(departments_df,
                                                         on="department_id",
                                                         how="left")
    grouped_df = employees_joined_departments_df.groupby(["department_id", "department"]).size().\
        reset_index(name="hired")
    grouped_df = grouped_df.sort_values(by="hired", ascending=False)
    result_df = grouped_df.query("hired > hired.mean()")
    return result_df
