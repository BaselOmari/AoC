from time import sleep

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

diff_list = [0,0,0]

while jolt is not device_jolt:
    for j in range(1,4):
        if find_jolt(jolt,j):
            diff_list[j-1] += 1
            jolt += j
            break

diff_list[2] += 1

print(diff_list[0]*diff_list[2])