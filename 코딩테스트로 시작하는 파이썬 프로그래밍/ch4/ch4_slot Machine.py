
chip = int(input())
count_1 = int(input())
count_2 = int(input())
count_3 = int(input())
machine = 1
play = 0
while chip >= 1:
    chip = chip - 1
    play = play + 1
    if machine ==1:
        count_1 = count_1 + 1
        if count_1 == 35:
            chip = chip + 30
            count_1 = 0
    elif machine == 2:
        count_2 = count_2 + 1
        if count_2 == 100:
            chip = chip + 60
            count_2 = 0
    elif machine == 3:
        count_3 = count_3 + 1
        if count_3 == 10:
            chip = chip + 9
            count_3 = 0

    if machine == 3:
        machine =1
    else: 
        machine = machine + 1

print('Martha plays {} times before going broke.'.format(play))
