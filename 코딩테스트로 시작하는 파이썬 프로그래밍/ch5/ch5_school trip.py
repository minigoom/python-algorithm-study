
import math
for i in range(10):
    compare = int(input())
    ratio_1,ratio_2, ratio_3, ratio_4 = (input().split(' '))
    num_student = int(input())
    # print('ratio_type:', type(ratio_1))
    num_1 = math.floor(num_student * float(ratio_1))
    num_2 = math.floor(num_student * float(ratio_2))
    num_3 = math.floor(num_student * float(ratio_3))
    num_4 = math.floor(num_student * float(ratio_4))
    num = []
    num.append(num_1)
    num.append(num_2)
    num.append(num_3)
    num.append(num_4)
    if num_student > sum(num):
        minus = num_student - sum(num)
        most = max(num)
        where = num.index(most)
        num[where] = num[where] + minus

    total = num[0]* 12 + num[1]* 10 + num[2]*7 + num[3]* 5
    if compare > (0.5*total):
        print('YES')
    else:
        print('NO')
    # print(num[0])
    # print(num[1])
    # print(num[2])
    # print(num[3])