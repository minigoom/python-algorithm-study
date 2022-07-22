# - ccc20j2
compare = int(input())
infected = int(input())
person_per_infect = int(input())
zero_day = infected
day = 0
sum = infected
while sum <= compare:
    sum = sum + infected*person_per_infect
    infected = infected*person_per_infect
    day = day + 1
    
    # print('sum:{}'.format(sum))
    # print('infected:{}'.format(infected))
    # print('day:{}'.format(day))
    # print('----')

print(day)