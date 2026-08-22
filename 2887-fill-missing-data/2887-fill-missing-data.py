import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products.fillna({'quantity':0}, inplace = True)
    return products
    