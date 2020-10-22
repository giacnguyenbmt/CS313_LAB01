import pandas as pd
import math

def modify_missing_value(df):
    """
    Chuyển giá trị bị khuyết bằng NaN.
    """
    df = df.replace("?", float("nan"))
    for col in df.columns:
        try:
            df[[col]] = df[[col]].astype(float)
        except:
            pass
    return df

def get_type(df):
    """
    Phân loại kiểu dữ liệu cho thuộc tính.
    """
    data_types = ["numeric" if d != "object" else "nominal" for d in df.dtypes]
    return data_types

def sum_col(arr, count=False):
    """
    Tính tổng giá trị khác NaN của một mảng Numpy array.
    """
    if str(type(arr)) == "<class 'pandas.core.frame.DataFrame'>":
        arr = arr.values.T[0]
    elif str(type(arr)) == "<class 'pandas.core.series.Series'>":
        arr = arr.values
    sum_ = 0
    count = 0
    for i in arr:
        if not math.isnan(i):
            sum_ += i
            count += 1
    if count is True:
        return sum_, count
    else:
        return sum_