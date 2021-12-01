from copy import deepcopy

with open("DATA/Day11Data.txt", 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]

for li, line in enumerate(data):
    data[li] = [seat for seat in line]

def range_checker(position, direction, seating_arrangment):
    checked_position = position.copy()
    while True:
        checked_position[0] += direction[0]
        checked_position[1] += direction[1]

        if not (checked_position[0] >= 0 and checked_position[0] < len(seating_arrangment[0]) and checked_position[1] >= 0 and checked_position[1] < len(seating_arrangment)):
            break

        if seating_arrangment[checked_position[1]][checked_position[0]] != '.':
            if seating_arrangment[checked_position[1]][checked_position[0]] == '#':
                return 1
            return 0

    return 0

def changing_seats(seating_arrangment):
    new_sa = deepcopy(seating_arrangment)
    
    for row in range(len(seating_arrangment)):
        for col in range(len(seating_arrangment[row])):
            available_surround = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]         
            occ_seats = 0

            for add in available_surround:
                if add == 0:
                    continue
                else:
                    occ_seats += range_checker([col,row],add,seating_arrangment)
                
            if seating_arrangment[row][col] == 'L' and occ_seats == 0:
                new_sa[row][col] = '#'
            elif seating_arrangment[row][col] == '#' and occ_seats >= 5:
                new_sa[row][col] = 'L'


    return new_sa

def data_printer(data):
    for row in data:
        for col in row:
            print(col, end = '')
        print()

def are_same(first,second):
    for x in range(len(first)):
        for y in range(len(first[x])):
            if first[x][y] != second[x][y]:
                return False
    
    return True

old_seats = data
final_seats = []

while True:
    new_seats = changing_seats(old_seats)

    if are_same(old_seats,new_seats):
        print(sum(x.count('#') for x in new_seats))
        break
    else:
        old_seats = deepcopy(new_seats)
