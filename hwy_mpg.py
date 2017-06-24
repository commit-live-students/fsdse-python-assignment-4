import pandas as pd
def calculateAvgHwy(file):
    df = pd.read_csv(file)
    dic = df[['hwy','class']].groupby('class').mean().to_dict()
    return dic['hwy']

#calculateAvgHwy("mpg.csv")
# Output: {'2seater': 24.800000000000001,
#  'compact': 28.297872340425531,
#  'midsize': 27.292682926829269,
#  'minivan': 22.363636363636363,
#  'pickup': 16.878787878787879,
#  'subcompact': 28.142857142857142,
#  'suv': 18.129032258064516}
