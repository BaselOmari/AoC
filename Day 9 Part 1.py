with open("DATA/Day9Data.txt", 'r') as f:
    data = f.readlines()

data = [int(line.strip()) for line in data]

def sum_check(number, array):
    for i_1 in range(len(array)):
        for i_2 in range(i_1):
            if array[i_1] + array[i_2] == number:
                return True
    return False

for i in range(len(data)-25):
    s_array = data[i:i+25]
    s_num = data[i+25]
    if not sum_check(s_num,s_array):
        print(s_num)