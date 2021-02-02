from typing import List

import csv

with open('advent/day2datadone.csv', 'r', encoding= 'utf-8-sig') as csvfile:
    csvreader = csv.reader(csvfile)
    data = list(csvreader)
    yes: int = 0
    no: int = 0
    for item in data:
        low = int(item[0])
        high = int(item[1])
        letter = item[2]
        string = item[3]
    
        if string[low - 1] == letter and string[high - 1] != letter:
            yes = yes + 1
        elif string[high - 1] == letter and string[low - 1] != letter:
            yes = yes + 1
        else:
            no += 1

    print(yes)

