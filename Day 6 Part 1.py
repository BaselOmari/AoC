with open('Day6Data.txt') as f:
    data = f.readlines()

data = [line.strip() for line in data]

total = 0
letters = []

for line in data:
    if line != '':
        for letter in line:
            letters.append(letter)
    else:
        letters = set(letters)
        total += len(letters)
        letters = []

letters = set(letters)
total += len(letters)

print(total)
