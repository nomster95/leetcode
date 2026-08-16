import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    a = customers.drop_duplicates(subset='email')
    return a
    