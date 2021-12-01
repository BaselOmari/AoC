with open("DATA/Day12Data.txt", 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]
data = [[line[:1],int(line[1:])] for line in data]

x_val = 0
y_val = 0

w_x = 10
w_y = 1

def rotate_right(point, times):
    for i in range(times):
        point[0], point[1] = point[1], -point[0]
    
    return point

def rotate_left(point,times):
    for i in range(times):
        point[0],point[1] = -point[1], point[0]
    
    return point

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
    elif action == 'R':
        normalized_value = value//90
        w_x,w_y = rotate_right([w_x,w_y], normalized_value)
    elif action == 'L':
        normalized_value = value//90
        w_x,w_y = rotate_left([w_x,w_y], normalized_value)

print(abs(x_val)+abs(y_val))