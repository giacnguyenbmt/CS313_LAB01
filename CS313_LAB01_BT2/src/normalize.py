#import thư viện cần thiết
import numpy as np
import pandas as pd

def normalize(Input, Output, Log):
    df = pd.read_csv(Input)