#Useful pieces of Python code: 

## Lookup table preparation
### Remove white spaces
#### strip_whitespace is a function to remove leading and trailing white space from all string columns in a DataFrame. This is particularly useful to run on lookup tables before trying to merge with administrative datasets of interest 
#### Found at GeeksForGeeks.org (https://www.geeksforgeeks.org/pandas-strip-whitespace-from-entire-dataframe/)

import pandas as pd

def strip_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    """Strip leading and trailing whitespace from all string columns in a DataFrame."""
    return df.apply(
        lambda col: col.str.strip() if col.dtype == "object" else col
    )