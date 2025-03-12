import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:

    if trips.empty or users.empty:
        return pd.DataFrame(columns=[\Day\, \Cancellation Rate\])

    renamed_users_for_clients = users.rename(
        columns={\users_id\: \client_id\, \banned\: \client_banned\}
    )

    trips_with_clients = trips.merge(
        renamed_users_for_clients, on=\client_id\, how=\left\
    )

    renamed_users_for_drivers = users.rename(
        columns={\users_id\: \driver_id\, \banned\: \driver_banned\}
    )

    full_trips = trips_with_clients.merge(
        renamed_users_for_drivers, on=\driver_id\, how=\left\
    )

    filtered_trips = full_trips[
        (full_trips[\client_banned\] == \No\)
        & (full_trips[\driver_banned\] == \No\)
        & (full_trips[\request_at\].between(\2013-10-01\, \2013-10-03\))
    ]

    result = filtered_trips.groupby(\request_at\).apply(
        lambda group: pd.Series(
            {
                \Cancellation Rate\: round(
                    (group[\status\] != \completed\).sum() / len(group), 2
                )
            }
        )
    )

    if result.empty:
        return pd.DataFrame(columns=[\Day\, \Cancellation Rate\])
    else:
        return result.reset_index().rename(columns={\request_at\: \Day\})