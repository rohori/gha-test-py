import pandas
import numpy

def f(df_csv: str) -> pandas.DataFrame:
    df = pandas.read_csv(df_csv)
    return df.assign(a=numpy.arange(len(df)))

def g(x: int) -> str:
    return x
