with open("DATA/Day9Data.txt", 'r') as f:
    data = f.readlines()

data = [int(line.strip()) for line in data]
invalid_num = 0

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
        invalid_num = s_num
        break

def array_sum(number, array):
    sum = 0
    for i in array:
        sum += i
    
    if sum == number:
        return True

def min_max(array):
    min = array[0]
    max = array[0]

    for num in array:
        if num > max:
            max = num
        if num < min:
            min = num
    
    return (min, max)

for low in range(len(data)-1):
    for high in range(low+2,len(data)+1):
        sliced_array = data[low:high]
        if array_sum(invalid_num, sliced_array):
            print(min_max(sliced_array)[0] + min_max(sliced_array)[1])
            break
