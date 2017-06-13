import pandas as pd

def calculateAvgHwy(path):
    data = pd.read_csv(path)
    avgData = data[['hwy','class']]
    avgData = avgData.groupby('class').mean()
    avgData = avgData.to_dict()
    return avgData['hwy']


calculateAvgHwy("./files/mpg.csv")
