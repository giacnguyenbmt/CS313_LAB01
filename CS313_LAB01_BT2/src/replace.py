import pandas as pd
import numpy as np
import math
import src.preprocessing as pc


def fill_numeric(arr):
    """
    Thay giá trị bị khuyết của mảng arr bằng giá trị trung bình.
    """
    sum_, count = pc.sum_col(arr, True)
    mean = sum_ / count
    for i in range(len(arr)):
        if math.isnan(arr[i]):
            arr[i] = mean
    return arr, round(mean, 2), len(arr) - count


def unique(arr):
    """
    Đếm số lần xuất hiện của các giá trị trong mảng arr.
    """
    counts = dict()
    for i in arr:
        if type(i) is str:
            counts[i] = counts.get(i, 0) + 1
    return sorted(counts.items(), reverse=True, key=lambda a: a[1])


def fill_nominal(arr):
    """
    Thay giá trị bị khuyết của mảng arr bằng giá trị xuất hiện nhiều nhất.
    """
    unique_list = unique(arr)
    value = unique_list[0][0]
    for i in range(len(arr)):
        if type(arr[i]) is not str:
            arr[i] = value
    return arr, value, len(arr) - sum([i for _, i in unique_list])


def replace(Input, Output, Log):
    """
    Thực hiện replace, lưu dữ liệu Output và ghi thông tin ra log file.
    """
    df = pd.read_csv(Input)
    df = pc.modify_missing_value(df)
    data_types = pc.get_type(df)[:-1]
    columns = df.columns[:-1]
    with open(Log, 'w', encoding="utf8") as f:
        for i in range(len(data_types)):
            if data_types[i] == "numeric":
                df.iloc[:, i], value, count = fill_numeric(df.iloc[:, i].to_numpy())
            else:
                df.iloc[:, i], value, count = fill_nominal(df.iloc[:, i].to_numpy())
            f.write("Thuộc tính: {:>10}, {:>4}, {:>8}\n".format(columns[i], count, value))
        f.close()
    df.to_csv(Output, index=False)