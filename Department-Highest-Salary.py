import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
    # joining the two tables
    df_merged = pd.merge(employee, department, left_on = 'departmentId', right_on = 'id')

    # sorting salary by department and salary
    df_sort = df_merged.sort_values(by = ['departmentId', 'salary'], ascending = False)

    # finding the max salary for each department
    max_salary = df_sort.groupby('departmentId')['salary'].transform('max')

    # returning first entry for each department
    df_first = df_sort[(df_sort['salary'] == max_salary)]

    return df_first[['name_y', 'name_x', 'salary']].rename(columns = {'name_y' : 'Department', 'name_x' : 'Employee', 'salary' : 'Salary'})

