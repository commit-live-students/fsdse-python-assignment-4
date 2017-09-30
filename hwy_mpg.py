import csv

def calculateAvgHwy(file_path):
    output = {}
    with open(file_path, 'rb') as csvfile:
        lines = [row for row in csv.reader(csvfile, delimiter=',')]

    for y in set([str(i[11]) for i in lines[1:]]):  # Itereate over vehicle class and set them
        val = [int(x[9]) for x in lines[1:] if x[11] == y]  # val = hwy mpg of given vehicle class
        output[y] = sum(val) / float(len(val))  # avg of mpg for given vehicle class

    return output



calculateAvgHwy('./files/mpg.csv')
