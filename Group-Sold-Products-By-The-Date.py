import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    act_agg = activities.sort_values(by='product').drop_duplicates(subset = ['sell_date', 'product'])

    act_agg = act_agg.groupby('sell_date').agg(products = ('product', ','.join), num_sold = ('product', 'count')).reset_index()

    return act_agg[['sell_date', 'num_sold', 'products']]