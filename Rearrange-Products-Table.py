import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products_melt = pd.melt(products, id_vars = 'product_id', var_name = 'store', value_name = 'price')

    # getting rid of nulls

    products_filtered = products_melt[products_melt['price'].notna()]

    return products_filtered