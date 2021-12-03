with open('input.txt') as f:
    instructions = [i.split() for i in f.readlines()]

instructions = [[i[0], int(i[1])] for i in instructions]

h = v = 0
for ist in instructions:
    if (ist[0] == 'forward'):
        h += ist[1]
    elif (ist[0] == 'up'):
        v -= ist[1]
    else:
        v += ist[1]

print(h*v)