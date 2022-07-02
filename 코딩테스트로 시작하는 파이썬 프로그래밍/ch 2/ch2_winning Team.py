# 6개의 숫자를 받는다
x_1 = int(input())
x_2 = int(input())
x_3 = int(input())
y_1 = int(input())
y_2 = int(input())
y_3 = int(input())
sum_x = x_1*3 + x_2*2 + x_3*1
sum_y = y_1*3 + y_2*2 + y_3*1
if sum_x > sum_y:
    print('A')
elif sum_x < sum_y:
    print('B')
else:
    print('T')