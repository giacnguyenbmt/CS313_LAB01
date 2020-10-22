import pandas as pd
import numpy as np
import src.preprocessing as pc


def EqualDepth():
    pass

def EqualWidth():
    pass

def discretize(Input, Output, Log):

    # Nhập số lượng giỏ
    num_bin = 0
    while num_bin < 1:
        try:
            num_bin = int(input("So gio: "))
        except:
            print("Type error!")
    # Nhập phương pháp chia:
    method = ""
    while method not in ["EqualDepth", "EqualWidth"]:
        try:
            method = input('Phuong phap chia (EqualDepth, EqualWidth): ')
        except:
            print("Input error!")
    if method == "EqualDepth":
        Depth = int(input("Depth = "))
    else:
        Width = float(input("Width = "))
