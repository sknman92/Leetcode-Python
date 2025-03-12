import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    df = employee

    # removing duplicates

    df_drop = df.drop_duplicates(subset = ['salary'])

    # finding nlargest

    df_largest = df_drop.nlargest(N, 'salary')

    # adjusting column name

    df_largest = df_largest[['salary']].rename(columns = {'salary' : f'getNthHighestSalary({N})'})
    
    # if above has one row, return none; else return the Nth row

    if len(df_largest) < N or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    else:
        return df_largest.iloc[[N-1]]