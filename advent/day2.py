from typing import List

import csv

with open('advent/day2datadone.csv', 'r', encoding= 'utf-8-sig') as csvfile:
    csvreader = csv.reader(csvfile)
    data = list(csvreader)
    yes: int = 0
    no: int = 0
    for item in data:
        item[0] = int(item[0])
        item[1] = int(item[1])
        count = item[3].count(item[2])
        if count >= item[0] and count <= item[1]:
            yes += 1
        else:
            no += 1

    print(yes)



    

