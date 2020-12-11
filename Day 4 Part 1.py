with open('Day4Data.txt') as f:
    passport_info = f.readlines()

passport_info = [passport.strip() for passport in passport_info]

new_passport_info = []

passport_detail = ''

for line in passport_info:
    if line == '':
        new_passport_info.append([passport_detail])
        passport_detail = ''
    passport_detail += line
    passport_detail += ' '

new_passport_info.append([passport_detail])

for passport in new_passport_info:
    for i in range(len(passport[0])):
        if passport[0][i] == ':':
            passport.append(i)

correct_passports_num = 0

for passport in new_passport_info:
    if len(passport) < 8:
        continue
    elif len(passport) == 9:

        correct_passports_num += 1
    else:
        correct = True
        for index, pi in enumerate(passport):
            if index == 0:
                continue
            key = passport[0][pi - 3:pi]
            if key == 'cid':
                correct = False
                break

        if correct:
            correct_passports_num += 1


print(correct_passports_num)