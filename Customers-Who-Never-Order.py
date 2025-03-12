import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df_merge = pd.merge(customers, orders, right_on = 'customerId', left_on='id', how = 'left')

    df_filtered = df_merge[df_merge['customerId'].isna()]

    df_answer = df_filtered[['name']].rename(columns = {'name' : 'Customers'})

    return df_answer