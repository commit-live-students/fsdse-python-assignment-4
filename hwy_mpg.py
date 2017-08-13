import csv


def calculateAvgHwy(csv_path):
    f = open(csv_path, 'rt')
    dict_reader = csv.DictReader(f)
    agg_hwy = {}
    count_hwy = {}
    for row in dict_reader:
        hwy = float(row['hwy'])
        v_class = row['class']
        if agg_hwy.has_key(v_class):
            agg_hwy[v_class] += hwy
            count_hwy[v_class] += 1.0
        else:
            agg_hwy[v_class], count_hwy[v_class] = hwy, 1.0

    return {hwy: agg_hwy[hwy] / count_hwy[hwy] for hwy in agg_hwy}

print calculateAvgHwy('./files/mpg.csv')
