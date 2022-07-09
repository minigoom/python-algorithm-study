chip = int(input())
count_1 = int(input())
count_2 = int(input())
count_3 = int(input())
play = 0 # 출력해야할 값 총 play 한 수를 나타낸다
machine =1 # 초기값 머신 1로 둔다

while chip > 0: # 칩이 있는동안 돌아간다.
    if machine == 1:
        chip = chip -1
        play = play + 1
        print('machine=1')
        machine = machine + 1
        count_1 = count_1 + 1
        if count_1 == 35:
            chip = chip + 30
            count_1 = 0

    elif machine == 2:
        chip = chip -1
        play = play + 1
        print('machine=2')
        machine = machine + 1
        count_2 = count_2 + 1
        if count_2 == 100:
            chip = chip + 60
            count_2 = 0

    elif machine == 3:
        chip = chip -1
        play = play + 1
        print('machine=3')
        machine = machine + 1
        count_3 = count_3 + 1
        if count_3 == 10:
            chip = chip + 9
            count_3 = 0
        if machine == 4:
            machine = 1
print(play)