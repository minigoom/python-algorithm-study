space = int(input())
yes = input()
tod = input()
yes = list(yes)
tod = list(tod)
# print(yes)
# print(tod)
# 문제 : 어제랑 오늘 모두 점유된 공간을 출력하여라
count = 0

for yes, tod in zip(yes,tod):
    if yes == tod and yes == 'C':
        count = count + 1
        # print(count)
    else:
        count = count + 0


print(count)
    