import pandas as pd

class DescribeData:
    def describe_data(datapath):
        raw_data = pd.read_csv(datapath)
        #print(raw_data)
        print('_' * 50)
        print(raw_data.info())
        print('_' * 50)
        print(raw_data.describe())
        print('_' * 50)
        #print(raw_data.plot.line())


        return raw_data, raw_data.plot.line(linewidth = 0.1)

if __name__ == "__main__":
    print("You meant to import this")