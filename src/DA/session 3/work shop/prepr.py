import pandas as pd

def drop_cols(df, cols):
    return df.drop(columns=cols)


def get_infoo(df):
    dtype = df.dtypes
    nunique = df.nunique()

    return pd.DataFrame({
        "nunique": nunique,
        "dtype": dtype
    }).T