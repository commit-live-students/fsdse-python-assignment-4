import pandas as pd

def calculateAvgHwy(input_file):
    raw_data = pd.read_csv(input_file)
    avg_of_Data = raw_data[['hwy','class']]
    avg_of_Data = avg_of_Data.groupby('class').mean()
    avg_of_Data = avg_of_Data.to_dict()
    return avg_of_Data['hwy']
