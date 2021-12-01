with open('Day2Data.txt') as f:
    lines = f.readlines()

passwords = [line.strip() for line in lines]

all_passwords = []

for password in passwords:
    dash = 0
    colon = 0

    for i in range(len(password)):
        if password[i] == '-':
            dash = i
        elif password[i] == ':':
            colon = i

    num_1 = int(password[:dash])
    num_2 = int(password[dash + 1:dash + 3])
    letter = password[colon - 1:colon]
    password_string = password[colon + 2:]

    # Entry 1: Position 1
    # Entry 2: Position 2
    # Entry 3: Letter in Question
    # Entry 4: Password
    password_info = [num_1,num_2,letter,password_string]
    all_passwords.append(password_info)


correct_passwords = 0

for password in all_passwords:
    pos_1 = password[0]
    pos_2 = password[1]
    character = password[2]
    password_string = password[3]


    if password_string[pos_1-1] == character or password_string[pos_2-1] == character:
        if not(password_string[pos_1-1] == character and password_string[pos_2-1] == character):
            correct_passwords += 1

print(correct_passwords)