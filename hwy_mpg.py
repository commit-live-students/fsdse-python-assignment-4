import csv

path = 'files/mpg.csv'

def calculateAvgHwy(path):
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        list1 = []
        cl = set()
        sdict = dict()
        results = [None] * 7
        for i in reader:
            list1.append([i['hwy'], i['class']])
            cl.add(i['class'])
        for j in cl:
            sdict.update({ j : [0,0]})
        for k in list1:
            tval = sdict[k[1]]
            tval[0] += float(k[0])
            tval[1] += 1
            sdict.update({k[1] : tval})

        for key in sdict:
            sdict.update({key: sdict[key][0]/sdict[key][1]})
        return sdict

print(calculateAvgHwy(path))
