import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    
    df_sorted = queue.sort_values(by = 'turn', ascending = True)

    df_sorted['running_weight'] = df_sorted['weight'].cumsum()

    df_filtered = df_sorted[df_sorted['running_weight'] <= 1000]

    solution = df_filtered.nlargest(1, 'running_weight')[['person_name']]

    return solution