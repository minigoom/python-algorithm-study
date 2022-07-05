num = int(input())
stu_list = []
cor_list = []
for i in range(num):
    x = input()
    stu_list.append(x)
for j in range(num):
    y = input()
    cor_list.append(y)
# print(stu_list)
# print(cor_list)
count = 0
for stu, cor in zip(stu_list, cor_list):
    if stu == cor:
        count = count+1

print(count)
