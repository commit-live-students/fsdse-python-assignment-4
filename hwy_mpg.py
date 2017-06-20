import pandas as pd
def calculateAvgHwy(input_path):
    input_data = pd.read_csv(input_path)
    output_data = input_data[['hwy','class']].groupby('class').mean().to_dict()
    return output_data['hwy']

#calculateAvgHwy("./files/mpg.csv")
