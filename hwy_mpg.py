import csv
def calculateAvgHwy(filename):
    with open(filename) as csvfile:
        data=list(csv.DictReader(csvfile))
    dic1={}
    vehicleclass=list(set(d['class'] for d in data))
    for i in vehicleclass:
        sumvalue=0
        vclass=0
        mean=0
        for d in data:
            if d['class']==i:
                sumvalue+=float(d['hwy'])
                vclass+=1
                mean=sumvalue/vclass
                dic1[d['class']]=mean
    return dic1
