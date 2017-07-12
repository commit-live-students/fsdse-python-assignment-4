import csv
def calculateAvgHwy(filepath):
   with open(filepath) as f:
       reader = csv.reader(f)
       reader_as_list = list(reader)

   reader_as_list = reader_as_list[1:len(reader_as_list)]
   reader_as_list[0:5]
   avg_sum = {}
   avg_count = {}
   count = 0

   for item in reader_as_list:
       if item[11] in avg_sum.keys():
           avg_sum[item[11]] += float(item[9])
       else:
           avg_sum[item[11]] = float(item[9])
   for item in reader_as_list:
       if item[11] in avg_count.keys():
           avg_count[item[11]] += 1
       else:
           avg_count[item[11]] = 1

   result_dict = {}
   for key in avg_sum.keys():
       result_dict[key] = avg_sum[key]/avg_count[key]
   return result_dict
