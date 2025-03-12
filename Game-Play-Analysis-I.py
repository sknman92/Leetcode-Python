import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby('player_id')['event_date'].min().reset_index(name = 'first_login')

    return activity