import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    distinct_salaries = employee.drop_duplicates(subset=['salary']).sort_values(by=['salary'], ascending=False)[['salary']]
    
    if len(distinct_salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary' : [None]})
   
    else:
        return distinct_salaries[['salary']].iloc[[1]]\\
                .rename(columns={'salary' : 'SecondHighestSalary'})