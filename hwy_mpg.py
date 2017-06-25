import csv
def calculateAvgHwy(filepath):
    csv_list = []
    csv_dict = {}
    csv_dict1 = {}
    with open(filepath, 'rb') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            csv_list.append(row)
        header = csv_list.pop(0)
        for elem in csv_list:
            key = elem[11]
            value = float(elem[9])
#             csv_dict[key] = value
#             csv_dict1[key] = value
            if key in csv_dict:
                csv_dict[key] += value
                csv_dict1[key] += 1
            else:
                csv_dict[key] = value
                csv_dict1[key] = 1
        answer = dict((k, csv_dict[k]/csv_dict1[k]) for k in csv_dict1)
        return answer

filepath = 'files/mpg.csv'
calculateAvgHwy(filepath)
