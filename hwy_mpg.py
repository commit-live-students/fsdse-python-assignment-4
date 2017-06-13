
def calculateAvgHwy(filepath):
    import csv
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile)
        req_list = []
        classes = set()
        sum_dict = dict()
        results = [None] * 7
        for row in reader:
            req_list.append([row['hwy'], row['class']])
            classes.add(row['class'])
        for req_class in classes:
            sum_dict.update({req_class : [0, 0]})
        for item in req_list:
            temp = sum_dict[item[1]]
            temp[0] += float(item[0])
            temp[1] += 1
            sum_dict.update({item[1] : temp})
        for key in sum_dict:
            sum_dict.update({key: sum_dict[key][0]/sum_dict[key][1]})
    return sum_dict
