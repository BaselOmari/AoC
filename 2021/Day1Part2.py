with open('input.txt') as f:
    numbers = f.readlines()
m = [int(number.strip()) for number in numbers]


m = [m[i-1] + m[i] + m[i+1] for i in range(1, len(m)-1)]
sum = 0

for i in range(1,len(m)):
    if m[i] > m[i-1]:
        sum += 1

print(sum)
