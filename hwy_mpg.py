import csv
import re
import numpy as np
def calculateAvgHwy(pth):
    f = open(pth,'r')
    veh_type = set()
    avg = 0.0
    dic = {}
    veh = np.genfromtxt(pth,delimiter=',',skip_header=1,dtype='|S20')
    s = set(veh[:,11])
    print s
    k=0
    for e in s:
        cnt = 0
        av_sum = 0.0
        for k in range(0,234):
            if veh[k,11] == e :
                av_sum = av_sum+int(veh[k,9])
                cnt = cnt+1
        #print(e,cnt,(av_sum/cnt))
        dic.update({e.replace('"',''):(av_sum/cnt)})

    print dic
    print dic['minivan']
    return dic
    #print veh





calculateAvgHwy('files/mpg.csv')
