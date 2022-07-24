for dataset in range(10):
    lst = input().split(' ')
    franch = int(lst[0])
    day = int(lst[1])

    grid = []
    for i in range(day):
        row = list(map(int, input().split()))
        grid.append(row)
    bonus = 0
    for row in grid:
        total = sum(row)
        if total % 13 == 0:
            bonus = bonus + total//13

    ###
    # print('grid:',grid)
    
    for col_index in range(franch): # - 0,1,2,3,
        total = 0
        for row_index in range(day): # - 0,1
            total = total + grid[row_index][col_index]

        if total % 13 == 0:
            bonus = bonus + total // 13
        
    print(bonus)



