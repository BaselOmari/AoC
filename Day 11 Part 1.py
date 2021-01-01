with open("DATA/Day11Data.txt", 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]

for li, line in enumerate(data):
    data[li] = [seat for seat in line]

def changing_seats(seating_arrangment):
    new_sa = seating_arrangment.copy()
    
    for row in range(len(seating_arrangment)):
        for col in range(len(seating_arrangment[row])):
            available_surround = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]
            if row == 0:
                available_surround[0], available_surround[1], available_surround[7] = 0,0,0
            elif row == (len(seating_arrangment[row])-1):
                available_surround[3], available_surround[4], available_surround[5] = 0,0,0
            
            if col == 0:
                available_surround[7], available_surround[6], available_surround[5] = 0,0,0
            elif col == (len(seating_arrangment)-1):
                available_surround[1], available_surround[2], available_surround[3] = 0,0,0
            
            # [Number of Occupied, Number of Empty]
            seats = [0,0]

            for add in available_surround:
                if add == 0:
                    continue

                



            


while True:
