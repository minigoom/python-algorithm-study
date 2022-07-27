for i in range(10):
    lst = input().split(' ')

    t = int(lst[0])
    n = int(lst[1])
    cat = 0
    for i in range(n):
        buy_or_not = input()
        if buy_or_not == "B":
            cat = cat + t - 1
        else:
            if cat > 0:
                cat = cat - 1

    print(cat)