import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset = 'salary')
    df = employee.sort_values(by = 'salary',ascending = False)
    if N<=0 or len(df) < N:

        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    return pd.DataFrame({f'getNthHighestSalary({N})': [df.iloc[N-1]['salary']]})