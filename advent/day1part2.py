from typing import List

import csv

def convert_to_list() -> int:
    with open('advent/data.csv', 'r') as f:
        reader = csv.reader(f)
        new_list: List[int] = []
        for row in reader:
            for item in row:
                new_list.append(item)

        for i in range(1, len(new_list)): 
            new_list[i] = int(new_list[i]) 
        
        y: int = 1
        i: int = 0
        x: int = 2
        z: int = 3
        while i < len(new_list):
            if z == 200:
                x += 1
                i = 0
                z = x + 1
            elif x == 200:
                z = 3
                y += 1
                i = 0
                x = y + 1
            elif new_list[y] + new_list[x] + new_list[z] == 2020:
                print("The answer is: ")
                return new_list[y] * new_list[x] * new_list[z]
            else:
                z += 1
                i += 1