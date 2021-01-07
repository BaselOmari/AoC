with open("DATA/Day12TestData.txt", 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]
data = [[line[:1],int(line[1:])] for line in data]

x_val = 0
y_val = 0

w_x = 10
w_y = 1

for command in data:
    action = command[0]
    value = command[1]
    
    if action == 'F':
        x_val += w_x*value
        y_val += w_y*value
    elif action == 'E':
        w_x += value
    elif action == 'W':
        w_x -= value
    elif action == 'N':
        w_y += value
    elif action == 'S':
        w_y -= value
    
    value //= 90
    value %= 4

    if value == 1:
        w_x, w_y = w_y, w_x
        w_x *= -1
    elif value == 2:
        w_x *= -1
        w_y *= -1
    elif value == 3:
        w_x, w_y = w_y, w_x
        w_y *= -1
    
    if action == 'R' and (value == 1 or value == 3):
        w_x *= -1
        w_y *= -1

print(abs(x_val)+abs(y_val))