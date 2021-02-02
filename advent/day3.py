from typing import List

import csv

with open('advent/day3data2.csv', 'r', encoding= 'utf-8-sig') as f:
    reader = csv.reader(f)
    start: int = 3
    yes: int = 0
    i: int = 0
    for row in reader:
        if start >= len(row):
            start = start - len(row)
            print(start)
        elif row[start] == '#':
            yes +=1
            start += 3
        else: 
            start += 3
            i += 1


print(yes)


with open('advent/day3data2.csv', 'r', encoding= 'utf-8-sig') as f:
  
  # X positions, iterator
  x_1 = 0
  x_3 = 0
  x_5 = 0
  x_7 = 0
  x_1_2 = 0
  i = 0

  # Tree counts
  trees_1 = 0
  trees_3 = 0
  trees_5 = 0
  trees_7 = 0
  trees_1_2 = 0
  
  for line in f:
    # Check for trees
    if line[x_1] == '#':
      trees_1 += 1
    if line[x_3] == '#':
      trees_3 += 1
    if line[x_5] == '#':
      trees_5 += 1
    if line[x_7] == '#':
      trees_7 += 1
    if i % 2 == 0 and line[x_1_2] == '#':
      trees_1_2 += 1

    # Adjust x movement with wraparound
    x_1 = (x_1 + 1) % (len(line) - 1)
    x_3 = (x_3 + 3) % (len(line) - 1)
    x_5 = (x_5 + 5) % (len(line) - 1)
    x_7 = (x_7 + 7) % (len(line) - 1)
    if i % 2 == 0:
      x_1_2 = (x_1_2 + 1) % (len(line) - 1)

    i += 1

  print("Part 1: ", trees_3)
  print("Part 2: ", trees_1 * trees_3 * trees_5 * trees_7 * trees_1_2)