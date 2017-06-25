import csv

def calculateAvgHwy(filepath):
    with open(filepath) as file1:
        readCSV = csv.reader(file1)
        cars = list(readCSV)
        cars = cars[1:]
        average_hwy ={}
        class_list = []
        counts2 = {}

        for sublist in cars:
            class1 = sublist[-1]
            hwy = sublist[-3]
            class_list.append(sublist[-1])

            if class1 in average_hwy:
                average_hwy[class1] += float(hwy)
                counts2[class1] += 1

            else:
                average_hwy[class1] = float(hwy)
                counts2[class1] = 1

        answer = dict((k, float(average_hwy[k]) / counts2[k]) for k in counts2)
    return answer
