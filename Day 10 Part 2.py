with open("DATA/Day10Data.txt",'r') as f:
    data = f.readlines()

data = [int(line.strip()) for line in data]

device_jolt = data[0]

for i in data:
    if i > device_jolt:
        device_jolt = i

jolt = 0

def find_jolt(joltage, add):
    required_jolt = joltage + add

    for i in data:
        if i == required_jolt:
            return True
    
    return False

def jolt_path(joltage):
    if joltage == device_jolt:
        return 0
    
    working_methods = 0
    for j in range(1,4):
        if find_jolt(joltage,j):
            working_methods += jolt_path(joltage+j) + 1
    
    working_methods -= 1
    
    return working_methods
    
print(jolt_path(0) + 1)