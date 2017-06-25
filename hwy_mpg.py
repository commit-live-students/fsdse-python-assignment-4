import pandas as pd
def calculateAvgHwy(file):
    df = pd.read_csv(file)
    dic = df[['hwy','class']].groupby('class').mean().to_dict()
    return dic['hwy']
