import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    article_views = views[ views['author_id'] == views['viewer_id'] ].groupby('author_id').first().reset_index()[['author_id']].sort_values(by='author_id').rename(columns = {'author_id' : 'id'})

    return article_views