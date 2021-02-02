
import csv

from typing import List

def range1(start, end):
    return range(start, end+1)

with open('advent/day6data.csv', 'r', encoding= 'utf-8-sig') as f:
    reader = csv.reader(f)
    ID_list: List[int] = []
    for row in reader:
        if row[0] == "F":
            lower1 = list(range1(0, 63))
        else:
            lower1 = list(range1(64, 128))
        
        if row[1] == "F":
            lower1 = list(range1(lower1[0], lower1[31]))
        else:
            lower1 = list(range1(lower1[32], lower1[63]))
        
        if row[2] == "F":
            lower1 = list(range1(lower1[0], lower1[15]))
        else:
            lower1 = list(range1(lower1[16], lower1[31]))
        
        if row[3] == "F":
            lower1 = list(range1(lower1[0], lower1[7]))
        else:
            lower1 = list(range1(lower1[8], lower1[15]))
        
        if row[4] == "F":
            lower1 = list(range1(lower1[0], lower1[3]))
        else:
            lower1 = list(range1(lower1[4], lower1[7]))

        if row[5] == "F":
            lower1 = list(range1(lower1[0], lower1[1]))
        else:
            lower1 = list(range1(lower1[2], lower1[3]))

        if row[6] == "F":
            lower1 = lower1[0]
        else:
            lower1 = lower1[1]
        
        if row[7] == "L":
            column = list(range1(0, 3))
        else:
            column = list(range1(4, 7))

        if row[8] == "L":
            column = list(range1(column[0], column[1]))
        else:
            column = list(range1(column[2], column[3]))

        if row[6] == "L":
            column = column[0]
        else:
            column = column[1]

        ID_number: int = (lower1 * 8) + column
        ID_list.append(ID_number)


    missing: List[int] = []
    there: List[int] = []
    
    for item in ID_list:
        i: int = 1000
        x: int = 0
        while i > x:
            if i - x == item:
                there.append(item)
                x = 1000
            elif x == 99:
                missing.append(item)
                x += 1
            else:
                x += 1

    print(len(missing))







        


        
            
            