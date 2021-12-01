with open('input.txt') as f:
    numbers = f.readlines()

numbers = [int(number.strip()) for number in numbers]
sum = 0

for i in range(1,len(numbers)):
    if numbers[i] > numbers[i-1]:
        sum += 1

print(sum)
