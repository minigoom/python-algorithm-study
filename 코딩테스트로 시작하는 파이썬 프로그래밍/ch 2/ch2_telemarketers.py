num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())

# 첫 번째 숫자는 8또는 9
con_1 = num_1 == 8 or num_1 == 9 # T, F 으로 출력
# print(con_1)

# 네 번째 숫자는 8또는 9
con_2 = num_4 == 8 or num_4 == 9 # T, F 으로 출력
# print(con_2)

# 두번째 세 번째 숫자는 동일
con_3 = num_2 == num_3
# print(con_3)

if con_1 and con_2 and con_3:
    print('ignore')
else:
    print('answer')