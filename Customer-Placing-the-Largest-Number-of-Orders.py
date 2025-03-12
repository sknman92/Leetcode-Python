import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby('customer_number').agg(cnt = ('order_number', 'count')).reset_index()

    orders = orders.nlargest(1, 'cnt')

    return orders[['customer_number']]