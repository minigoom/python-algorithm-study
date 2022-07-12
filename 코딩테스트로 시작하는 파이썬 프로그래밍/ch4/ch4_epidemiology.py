# p: 비교대상
# n : day 0 에 감염된 수
# R : 한명이 감염 시킬 수 있는 수

p = int(input())
n = int(input())
R = int(input())
# print('ok')
count = 0
x = 1
total_list =[]
total_list_sum = sum(total_list)

while p >= total_list_sum:
 
    day = n * (R**x)
    total_list.append(day)
    # print(total_list)
    total_list_sum = sum(total_list)
    # print(total_list_sum)
    x = x + 1
    count = count + 1
    # print(count)
print(count)