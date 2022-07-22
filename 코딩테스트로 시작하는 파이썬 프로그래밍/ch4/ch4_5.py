
for i in range(10):
    condition = True
    c_orange = 0
    c_blue = 0
    c_green = 0
    c_yellow = 0
    c_pink = 0
    c_violet = 0
    c_brown = 0
    c_red = 0
    while condition:
        color = input()
        if color == 'orange':
            c_orange += 1
        elif color == 'blue':
            c_blue += 1
        elif color == 'green':
            c_green += 1
        elif color == 'yellow':
            c_yellow += 1
        elif color == 'pink':
            c_pink += 1
        elif color == 'violet':
            c_violet += 1
        elif color == 'brown':
            c_brown += 1
        elif color == 'red':
            c_red += 1
        elif color == 'end of box':
            condition = False

    count = 0
    for i in [c_orange,c_blue, c_green, c_yellow, c_pink, c_violet, c_brown]:
        a, b = divmod(i,7)
        if b == 0:
            b = 0
        else:
            b = 1
        count = count + a + b
        

    answer = (13 * count) + (16 *c_red)
    print(answer)