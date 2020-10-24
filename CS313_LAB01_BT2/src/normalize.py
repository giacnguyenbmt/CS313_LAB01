import pandas as pd
import numpy as np
import src.preprocessing as pc


def Minmax(df, e=1e-10):
    """
    Chuẩn hoá dữ liệu theo phương pháp Min-max.
    """
    data = df.to_numpy()
    max_ = data.max(axis=0)
    min_ = data.min(axis=0)
    data = (data - min_) / (max_ - min_ + e)
    domain = ["[0.00, 1.00]" for i in range(data.shape[1])]
    return data, domain


def Zscore(df, e=1e-10):
    """
    Chuẩn hoá dữ liệu theo phương pháp Min-max.
    """
    data = df.to_numpy()
    means = data.sum(axis=0) / data.shape[0]
    std = np.sqrt(np.sum((data - means)**2, axis=0) / data.shape[0])
    data = (data - means) / (std + e)
    domain = ["[{}, {}]".format(m, n)
              for m, n in zip(data.min(axis=0).round(2),
                              data.max(axis=0).round(2))]
    return data, domain


def normalize(Input, Output, Log):
    """
    Thực hiện chức năng normalize, lưu dữ liệu Output và ghi thông tin ra log file.
    """
    df = pd.read_csv(Input)
    df = pc.modify_missing_value(df)
    data_types = np.array(pc.get_type(df))
    num_col = np.array(df.columns[data_types=='numeric'][:-1])
    method = pc.SelectValue(["Minmax", "Zscore"], mess="Select method")
    if method == "Minmax":
        df[num_col], domain = Minmax(df[num_col])
    else:
        df[num_col], domain = Zscore(df[num_col])
    df.to_csv(Output, index=False)
    with open(Log, 'w', encoding="utf8") as f:
        for i, col in enumerate(num_col):
            f.write("Thuộc tính: {:<20} {}\n".format(col, domain[i]))
    f.close()