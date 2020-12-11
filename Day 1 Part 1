with open('input.txt') as f:
    numbers = f.readlines()

numbers = [int(number.strip()) for number in numbers]

for i_1 in range(len(numbers)):
    for i_2 in range(i_1):
        if numbers[i_1] + numbers[i_2] == 2020:
            print(numbers[i_1], numbers[i_2])
