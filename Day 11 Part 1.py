from time import sleep
from copy import deepcopy

with open("DATA/Day11Data.txt", 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]

for li, line in enumerate(data):
    data[li] = [seat for seat in line]

def changing_seats(seating_arrangment):
    new_sa = deepcopy(seating_arrangment)
    
    for row in range(len(seating_arrangment)):
        for col in range(len(seating_arrangment[row])):
            available_surround = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]
            if row == 0:
                available_surround[0], available_surround[1], available_surround[7] = 0,0,0
            elif row == (len(seating_arrangment)-1):
                available_surround[3], available_surround[4], available_surround[5] = 0,0,0
            
            if col == 0:
                available_surround[7], available_surround[6], available_surround[5] = 0,0,0
            elif col == (len(seating_arrangment[row])-1):
                available_surround[1], available_surround[2], available_surround[3] = 0,0,0
            
            occ_seats = 0

            for add in available_surround:
                if add == 0:
                    continue
                else:
                    new_col = col + add[0]
                    new_row = row + add[1]
                    # print(new_col,new_row, add)
                    searched_seat = seating_arrangment[new_row][new_col]

                    if searched_seat == '#':
                        occ_seats += 1
                

            if seating_arrangment[row][col] == 'L' and occ_seats == 0:
                new_sa[row][col] = '#'
                # print("CHANGED")
            elif seating_arrangment[row][col] == '#' and occ_seats >= 4:
                new_sa[row][col] = 'L'
                # print("CHANGED")


            # print(col,row, seating_arrangment[row][col], new_sa[row][col])
            # data_printer(seating_arrangment)
            # print()
            # data_printer(new_sa)
            # print("ADDS:", available_surround)
            # print("OCC:", occ_seats)
            # print("\n\n")

            # sleep(7)


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
        final_seats = new_seats
        break
    else:
        # data_printer(old_seats)
        # print("\n\n")
        # data_printer(new_seats)
        # print()
        # sleep(20)
        old_seats = deepcopy(new_seats)
# 
print(sum(x.count('#') for x in final_seats))