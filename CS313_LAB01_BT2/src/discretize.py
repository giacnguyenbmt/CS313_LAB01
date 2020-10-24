import pandas as pd
import numpy as np
import src.preprocessing as pc


def EqualDepth(arr, num_bin):
    """
    Chia giỏ theo chiều sâu, trả về mảng các giỏ, miền giá trị và số lượng 
    phần tử mỗi giỏ.
    """
    mean = int(len(arr) // num_bin)
    depth = mean if len(arr) % num_bin == 0 else mean + 1
    enum_list = [i for i, _ in sorted(enumerate(arr), key=lambda x: x[1])]
    bin_ = []
    for i in range(0, len(arr), depth):
        bin_.append(list(enum_list[i:i+depth]))
    domain = []
    counts = []
    for i in bin_:
        counts.append(len(i))
        max_ = round(float(arr[i[-1]]), 2)
        min_ = round(float(arr[i[0]]), 2)
        domain.append("[{}, {}]".format(min_, max_))
    return bin_, domain, counts


def EqualWidth(arr, num_bin):
    """
    Chia giỏ theo chiều rộng, trả về mảng các giỏ, miền giá trị và số lượng 
    phần tử mỗi giỏ.
    """
    min_ = arr.min()
    max_ = arr.max()
    width = (max_ - min_) / num_bin
    
    if width == 0.0:
        bin_ = [list(range(len(arr)))]
        domain = ["[{}, {}]".format(0.0, 0.0)]
        counts = [len(arr)]
    else:
        bin_ = [[] for i in range(num_bin)]
        for i, val in sorted(enumerate(arr), key=lambda x: x[1]):
            index = int((val - min_) // width)
            if index == num_bin:
                bin_[index - 1].append(i)
            else:
                bin_[index].append(i)
                
        range_ = np.arange(min_, max_, width).round(2)
        domain = ["[{}, {})".format(range_[i], range_[i+1])
                  for i in range(len(range_)-1)]
        domain.append("[{}, {}]".format(range_[-1], 
                                        round(float(max_), 2)))
        counts = [len(b) for b in bin_]
    return bin_, domain, counts


def SmoothingByMeans(arr):
    """
    Làm trơn bằng giá trị trung bình giỏ.
    """
    return np.full(arr.shape, arr.mean())


def SmoothingByBoundaries(arr):
    """
    Làm trơn bằng biên giỏ.
    """
    new_val = arr.copy()
    for i in range(len(arr)):
        if (arr[i] - arr[0]) < (arr[-1] - arr[i]):
            new_val[i] = arr[0]
        else:
            new_val[i] = arr[-1]
    return new_val


def SmoothingByMedian(arr):
    """
    Làm trơn bằng trung tuyến giỏ.
    """
    return np.full(arr.shape, arr[len(arr)//2])


def ReplaceValue(bin_, arr, s_method):
    """
    Thay giá trị các phần tử bằng miền giá trị của giỏ tương ứng.
    """
    if s_method == "means":
        smoothing = SmoothingByMeans
    elif s_method == "boundaries":
        smoothing = SmoothingByBoundaries
    else:
        smoothing = SmoothingByMedian
        
    for b in bin_:
        if len(b) > 0:
            arr[b] = smoothing(arr[b])
    return arr


def discretize(Input, Output, Log):
    """
    Thực hiện chức năng discretize, lưu dữ liệu Output và ghi thông tin ra log file.
    """
    df = pd.read_csv(Input)
    df = pc.modify_missing_value(df)
    data_types = np.array(pc.get_type(df))
    num_col = np.array(df.columns[data_types=='numeric'][:-1])
    
    # Nhập số lượng giỏ
    num_bin = pc.InputValue(0, 1, "number of bins: ")
    # Nhập phương pháp chia:
    method = pc.SelectValue(["EqualDepth", "EqualWidth"], mess="Select binning method")
    # Nhập phương pháp làm trơn:
    s_method = pc.SelectValue(["means", "boundaries", "median"], mess="Select smoothing method")
    with open(Log, 'w', encoding="utf8") as f:
        for col in num_col:
            if method == "EqualDepth":
                bin_, domain, counts = EqualDepth(df[col].to_numpy(), num_bin)
            else:
                bin_, domain, counts = EqualWidth(df[col].to_numpy(), num_bin)
                
            f.write("Thuộc tính: {}\n".format(col))
            for i in range(len(bin_)):
                f.write("\t{:<20}:{:>5}\n".format(domain[i], counts[i]))
                
            df[col] = ReplaceValue(bin_, df[col].to_numpy(), s_method)
    f.close()
    df.to_csv(Output, index=False)
