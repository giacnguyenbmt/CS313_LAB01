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


def sum_col(arr, return_counts=False):
    """
    Tính tổng giá trị khác NaN của một mảng Numpy array.
    """
    if str(type(arr)) == "<class 'pandas.core.frame.DataFrame'>":
        arr = arr.values.T[0]
    elif str(type(arr)) == "<class 'pandas.core.series.Series'>":
        arr = arr.values
    sum_ = 0
    counts = 0
    for i in arr:
        if not math.isnan(i):
            sum_ += i
            counts += 1
    if return_counts is True:
        return sum_, counts
    else:
        return sum_


def InputValue(init_val, cond_val, mess="Input: ", dtype=True):
    """
    Nhập giá trị cho biến thoả mãn điều kiện cho trước.
    """
    input_val = init_val
    while input_val < cond_val:
        try:
            if dtype is True:
                input_val = int(input(mess))
            else:
                input_val = float(input(mess))
        except:
            print("Type error!")
    return input_val


def SelectValue(val_list, mess="Select"):
    """
    Lựa chọn giá trị cho biến thoả mãn điều kiện cho trước.
    """
    select_val = ""
    while select_val not in val_list:
        try:
            select_val = input('{} {}: '.format(mess, val_list))
        except:
            print("Input error!")
    return select_val