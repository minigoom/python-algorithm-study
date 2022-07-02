burger = input()
side = input()
drink = input()
dessert = input()

if burger:
    if burger == '1':
        cal_1 = 461
    elif burger == '2':
        cal_1 = 431
    elif burger == '3':
        cal_1 = 420
    else:
        cal_1 = 0
# print(cal_1)

if side:
    if side == '1':
        cal_2 = 100
    elif side == '2':
        cal_2 = 57
    elif side == '3':
        cal_2 = 70
    else:
        cal_2 = 0
# print(cal_2)

if drink:
    if drink == '1':
        cal_3 = 130
    elif drink == '2':
        cal_3 = 160
    elif drink == '3':
        cal_3 = 118
    else:
        cal_3 = 0
# print(cal_3)


if dessert:
    if dessert == '1':
        cal_4 = 167
    elif dessert == '2':
        cal_4 = 266
    elif dessert == '3':
        cal_4 = 75
    else:
        cal_4 = 0
# print(cal_4)
cal = cal_1 + cal_2 + cal_3 + cal_4
# print('Your total Calorie count is', cal,'.')   
print('Your total Calorie count is {}.'.format(cal))