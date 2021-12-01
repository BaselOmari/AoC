with open("DATA/Day8Data.txt", 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]


data = [[line[:3], int(line[4:])] for line in data]

visited_index = []
acc_val = 0

def in_visited(index):
    for i in visited_index:
        if i == index:
            return True
    
    return False

i = 0
while True:
    ting = data[i]
    visited_index.append(i)
    if ting[0] == 'acc':
        acc_val += ting[1]
    elif ting[0] == 'jmp':
        i += ting[1] - 1
    i += 1

    if in_visited(i):
        print(acc_val)
        break

    