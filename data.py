# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:13:00 2019

@author: ZHOU_YuZHAO
"""
import csv
import matplotlib.pyplot
data_line=[]
f=open("in.txt")
for each_line in f:
    data_line.append(each_line)

f.close()
    
    
w = open('data.csv' , 'w')
for new_line in  data_line:
    w.write(new_line)
w.close()

environment = []
with open('data.csv', newline='') as f:
    f = csv.reader(f)
    for row in f:
        row_list = []
        for values in row:
            row_list.append(int(values))
        environment.append(row_list)


#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
        

        