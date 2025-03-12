import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    # merging company and orders tables

    merge1 = pd.merge(orders, company, on = 'com_id')[['sales_id', 'name']]

    # merging with sales_person

    merge2 = pd.merge(merge1, sales_person, how = 'right',  on = 'sales_id')[['name_x', 'name_y']]

    # changing dtype of name_x

    merge2['name_x'] = merge2['name_x'].astype(str)

    # grouping by sales person and concat'ing company

    merge2 = merge2.groupby('name_y').agg(companies = ('name_x', ','.join)).reset_index()

    # excluding if red exists in company

    merge2 = merge2[~merge2['companies'].str.contains(r'\\bRED\\b')][['name_y']].rename(columns = {'name_y' : 'name'})

    return merge2