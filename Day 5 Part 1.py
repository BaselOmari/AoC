with open('Day5Data.txt') as f:
    boarding_pass = f.readlines()

boarding_pass = [bp.strip() for bp in boarding_pass]

max_id = 0

for bp in boarding_pass:
    min = 0
    max = 127

    for sym in bp[:7]:
        # print(sym)
        mid = (min+max)/2

        decimal = False
        if mid - int(mid) != 0:
            decimal = True

        if sym == 'F':
            max = int(mid)
        else:
            min = int(mid)
            if decimal:
                min += 1

    row = min

    min = 0
    max = 7

    for sym in bp[7:]:
        mid = (min + max) / 2

        decimal = False
        if mid - int(mid) != 0:
            decimal = True

        if sym == 'L':
            max = int(mid)
        else:
            min = int(mid)
            if decimal:
                min += 1

    col = min
    
    seat_id = (row*8) + col

    if seat_id > max_id:
        max_id = seat_id


print(max_id)

