# 카드 list

card_list = [ 1,2,3,4,5,6,7,8,9,10,10,10,10,11]*4
n = int(input())
total = 0
for i in range(n):
    rm_card = int(input())
    total = total + rm_card
    card_list.remove(rm_card)

diff = 21 - total
dos = 0
vi = 0
for i in card_list:
    if i > diff:
        dos += 1
    else:
        vi += 1

if dos > vi:
    print('DOSTA')
else:
    print('VUCI')
    