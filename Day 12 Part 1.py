with open("DATA/Day12Data.txt", 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]
data = [[line[:1],int(line[1:])] for line in data]

x_val = 0
y_val = 0
directions = ['E', 'N', 'W', 'S']
direction = 0

for command in data:
    action = command[0]
    value = command[1]

    if action == 'L':
        value //= 90
        direction += value
    elif action == 'R':
        value //= 90
        direction -= value
    
    elif action == 'F':
        d = direction%4
        print(type(d))
        action = directions[d]
    
    if action == 'E':
        x_val += value
    elif action == 'W':
        x_val -= value
    elif action == 'N':
        y_val += value
    elif action == 'S':
        y_val -= value
    


print(abs(x_val) + abs(y_val))


