import pandas as pd
def calculateAvgHwy(mpg):
    hwy=pd.read_csv(mpg)
    pivot=hwy.pivot_table(values='hwy',index=['class'])
    ans={}
    for i in hwy['class'].unique():
        ans[i]=pivot.loc[i]['hwy']
    return ans
