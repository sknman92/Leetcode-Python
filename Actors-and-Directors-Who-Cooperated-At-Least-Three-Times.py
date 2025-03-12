import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    
    actor_director = actor_director.groupby(['director_id', 'actor_id']).agg(cnt = ('actor_id', 'count')).reset_index()

    actor_director = actor_director[actor_director['cnt'] >= 3][['director_id', 'actor_id']]
    
    return actor_director