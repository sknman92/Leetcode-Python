import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    
        def triangle_func(row):

            if row.sum() > 2 * row.max():
                return 'Yes'
            else:
                return 'No'


        triangle['triangle'] =  triangle.apply(triangle_func, axis = 1)   
        return triangle