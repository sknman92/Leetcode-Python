import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # Cross join students and subjects
    df = pd.merge(students, subjects, how='cross')

    # calculating number of exams taken per student and subject
    df2 = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name = 'attended_exams')

    # merge examinations
    result = pd.merge(df, df2, how = 'left', on = ['student_id', 'subject_name'])

    # turn nulls to 0s
    result['attended_exams'] = result['attended_exams'].fillna(0)

    # sorting
    result.sort_values(by = ['student_id', 'subject_name'], inplace = True)

    return result
