import sys
from src import summary, replace, discretize, normalize

if __name__ == '__main__':
    argumentList = sys.argv[1:]
    if len(argumentList) == 3:
        Option, Input, Log = argumentList
        if Option == 'summary':
            # summary
            pass
        else:
            print("Option error!")
    else:
        Option, Input, Output, Log = argumentList
        if Option == 'replace':
            pass
        elif Option == 'discretize':
            pass
        elif Option == 'normalize':
            pass
        else:
            print("Option error!")