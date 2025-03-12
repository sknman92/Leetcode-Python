import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    # creating if-then function

    def category_function(x):
    
        if x < 20000:
            return 'Low Salary'
        elif x >= 20000 and x <= 50000:
            return 'Average Salary'
        else:
            return 'High Salary'

    # applying if-then statement

    accounts['category'] = accounts['income'].apply(category_function)

    # counting category

    category_counts = accounts['category'].value_counts()

    # all categories

    all_categories = ['Low Salary', 'Average Salary', 'High Salary']

    # reindexing according to all_categories

    category_filled = category_counts.reindex(all_categories).fillna(0).reset_index(name = 'accounts_count')

    return category_filled