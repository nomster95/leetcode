import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset = 'salary')
    df = employee.sort_values(by = 'salary',ascending = False)
    if len(df) < 2:

        return pd.DataFrame({'SecondHighestSalary': [None]})

    return pd.DataFrame({'SecondHighestSalary': [df.iloc[1]['salary']]})