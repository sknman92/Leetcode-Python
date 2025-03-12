import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    correct_mail = users[users['mail'].str.contains(r'^[a-zA-Z][\w\d_\.-]*@leetcode\.com$')]

    return correct_mail
