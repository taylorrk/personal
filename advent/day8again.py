
import csv
from typing import List
from io import StringIO
import numpy as np

d = np.recfromcsv('advent/day8data.csv', delimiter=',', encoding= 'utf-8-sig')

row: int = 0
acc_count: int = 0
i: int = 0
list_of_rows: List[int] = []
    
while i < 603:
    
    if row in list_of_rows:
        print(acc_count)
        i = 603
    
    elif d[row][0] == "acc":
        list_of_rows.append(row)
        if d[row][1] == "-":
            acc_count = acc_count - int(d[row][2])
            row += 1
            i += 1
        else:
            acc_count = acc_count + int(d[row][2])
            row += 1
            i += 1
    
    elif d[row][0] == "jmp":
        list_of_rows.append(row)
        if d[row][1] == "-":
            row = row - int(d[row][2])
            i += 1
        else:
            row = row + int(d[row][2])
            i += 1
    
    else:
        list_of_rows.append(row)
        row += 1
        i += 1





    