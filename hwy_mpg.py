import csv
def calculateAvgHwy(filepath):
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile)
        # reader.next()
        count = 0
        total = 0
        mydict = {}
        count_dict = {}
        for row in reader:
            if row["class"] in mydict:
                mydict[row["class"]] += int(row['hwy'])
                count_dict[row["class"]] += 1
            else:
                mydict[row["class"]] = int(row["hwy"])
                count_dict[row["class"]] = 1
        for key in mydict:
            mydict[key] = float(mydict[key])/count_dict[key]

        print mydict
        return mydict
