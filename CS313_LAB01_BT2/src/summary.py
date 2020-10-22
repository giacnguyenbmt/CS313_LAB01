import pandas as pd
import src.preprocessing as pc

def summary(Input, Log):
    """
    Thực hiện summary và ghi thông tin ra log file.
    """
    # Đọc dữ liệu với pandas
    df = pd.read_csv(Input)
    df = pc.modify_missing_value(df)

    # Lấy thông tin dữ liệu
    num_instance, num_attribute = df.shape
    num_attribute -= 1
    columns = df.columns[:-1]
    data_types = pc.get_type(df)[:-1]

    # Lưu thông tin ra log file
    with open(Log, 'w', encoding="utf8") as f:
            f.write("Số mẫu: {}\n".format(num_instance))
            f.write("Số thuộc tính: {}\n".format(num_attribute))
            for i in range(num_attribute):
                f.write("Thuộc tính {:>2}: {} - {}\n".format(i+1, columns[i], data_types[i]))
            f.close()