with open('Day6Data.txt') as f:
    data = f.readlines()

data = [line.strip() for line in data]

total = 0
letters = []
people_count = 0

for line in data:
    if line != '':
        people_count += 1
        for letter in line:
            letters.append(letter)
    else:
        ans_let = []
        for letter in letters:
            if letters.count(letter) == people_count:
                ans_let.append(letter)
        ans_let = set(ans_let)
        total += len(ans_let)

        letters = []
        people_count = 0


ans_let = []
for letter in letters:
    if letters.count(letter) == people_count:
        ans_let.append(letter)
ans_let = set(ans_let)
total += len(ans_let)

print(total)