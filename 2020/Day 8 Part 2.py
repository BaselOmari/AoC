with open("DATA/Day8Data.txt", 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]


data = [[line[:3], int(line[4:])] for line in data]


def in_visited(index, v_arr):
    for i in v_arr:
        if index == i[0]:
            i[1] += 1
            return
    v_arr.append([index, 0])

def greater_than(v_arr):
    for i in v_arr:
        if i[1] > 500:
            return True
    
    return False

def terminates(instructions):
    visited = []
    acc_val = 0
    i = 0

    while True:
        if i >= len(instructions):
            return [True, acc_val]
        
        in_visited(i, visited)
        if greater_than(visited):
            return [False]

        ting = instructions[i]
        desc = ting[0]
        val = ting[1]
        
        if desc == 'acc':
            acc_val += val
        elif desc == 'jmp':
            i += val - 1
        i += 1


for i in range(len(data)):
    nop_bool = False
    jmp_bool = False
    copy_data = data.copy()
    if copy_data[i][0] == 'nop':
        nop_bool = True
        copy_data[i][0] = 'jmp'

    elif copy_data[i][0] == 'jmp':
        jmp_bool = True
        copy_data[i][0] = 'nop'
    else:
        continue


    if terminates(copy_data)[0] == True:
        print(terminates(copy_data)[1])
        break

    print(i, "DONE")

    if nop_bool:
        copy_data[i][0] = 'nop'
    else:
        copy_data[i][0] = 'jmp'
