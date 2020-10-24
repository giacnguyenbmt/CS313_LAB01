import sys
from src import summary, replace, discretize, normalize


if __name__ == '__main__':
    # Lấy danh sách tham số
    argumentList = sys.argv[1:]
    # Thực hiện chức năng
    if len(argumentList) == 3:
        Option, Input, Log = argumentList
        if Option == 'summary':
            summary.summary(Input, Log)
        else:
            print("Option error!")
    elif len(argumentList) == 4:
        Option, Input, Output, Log = argumentList
        if Option == 'replace':
            replace.replace(Input, Output, Log)
        elif Option == 'discretize':
            discretize.discretize(Input, Output, Log)
        elif Option == 'normalize':
            normalize.normalize(Input, Output, Log)
        else:
            print("Option error!")