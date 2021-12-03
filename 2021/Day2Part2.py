with open('input.txt') as f:
    instructions = [i.split() for i in f.readlines()]

instructions = [[i[0], int(i[1])] for i in instructions]

h = a = d = 0
for ist in instructions:
    if (ist[0] == 'forward'):
        h += ist[1]
        d += ist[1]*a
    elif (ist[0] == 'up'):
        a -= ist[1]
    else:
        a += ist[1]

print(h*d)