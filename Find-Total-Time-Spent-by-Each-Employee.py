import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.assign(total_time = lambda x: x['out_time'] - x['in_time'])

    employees = employees.groupby(['event_day', 'emp_id']).agg({'total_time' : sum}).reset_index()

    employees = employees.rename(columns = {'event_day' : 'day'})

    return employees