with open('Day3Data.txt') as f:
    text = f.readlines()

trees = [row.strip() for row in text]

product = 1
right_slope = [[1,1],[3,1],[5,1],[7,1],[1,2]]

for slope in right_slope:
    trees_number = 0
    right_i = 0
    for index, row in enumerate(trees):
        if (index%slope[1] == 0):
            row_i = right_i%len(row)
            if row[row_i] == '#':
                trees_number += 1

            right_i += slope[0]
    product *= trees_number



print(product)