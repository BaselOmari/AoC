with open('Day3Data.txt') as f:
    text = f.readlines()

trees = [row.strip() for row in text]

trees_number = 0

right_i = 0

for row in trees:
    row_i = right_i%len(row)
    if row[row_i] == '#':
        trees_number += 1

    right_i += 3

print(trees_number)