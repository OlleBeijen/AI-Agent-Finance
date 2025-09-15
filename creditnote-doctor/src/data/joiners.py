
import pandas as pd

def left_join(left: pd.DataFrame, right: pd.DataFrame, on: list[str]):
    return left.merge(right, on=on, how="left", suffixes=("", "_r"))
