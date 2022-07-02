# 2월 18일 이전, 이후, special 출력
input_month = int(input())
input_day = int(input())

month = 2
day = 18
if input_month == 1:
    print('Before')
elif input_month ==2 and input_day < day:
    print('Before')
elif input_month == month and input_day == day:
    print('Special')
else:
    print('After')