import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
  answer = patients[patients['conditions'].str.contains(r'(?<!\+)\bDIAB1')]

  return answer