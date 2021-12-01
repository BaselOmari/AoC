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

correct_passports = []

for passport in new_passport_info:
    if len(passport) < 8:
        continue
    elif len(passport) == 9:
        correct_passports.append(passport)
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
            correct_passports.append(passport)


# print(correct_passports)


passport_details = []

for passport in correct_passports:
    pd = []
    passport_str = passport[0]

    for index in passport[1:]:
        key = passport_str[index-3:index]
        for i, space in enumerate(passport_str[index:]):
            if space == ' ':
                break

        info = passport_str[index+1:index+1+i]
        pd.append([key,info.strip()])

    passport_details.append(pd)

correct_passports_number = 0
for passport in passport_details:
    correct = True
    for detail in passport:
        key = detail[0]
        info = detail[1]

        if key == 'byr':
            info = int(info)
            if info > 2002 or info < 1920:
                correct = False
        elif key == 'iyr':
            info = int(info)
            if info < 2010 or info > 2020:
                correct = False

        elif key == 'eyr':
            info = int(info)
            if info < 2020 or info > 2030:
                correct = False

        elif key == 'hgt':
            unit = info[-2:]

            if unit == 'in':
                length = int(info[:len(info) - 2])
                if length < 59 or length > 76:
                    correct = False
            elif unit == 'cm':
                length = int(info[:len(info) - 2])
                if length < 150 or length > 193:
                    correct = False
            else:
                correct = False

        elif key == 'hcl':
            if info[0] != '#':
                correct = False
            else:
                for char in info[1:]:
                    char = ord(char)
                    if not ((char >= 97 and char <= 102) or (char >= 48 and char <= 57)):
                        correct = False

        elif key == 'ecl':
            if not (info == 'amb' or info == 'blu' or info == 'brn' or info == 'gry' or info == 'grn' or info == 'hzl' or info == 'oth'):
                correct = False

        elif key == 'pid':
            if len(info) != 9:
                correct = False

    if correct:
        correct_passports_number += 1





print(correct_passports_number)
