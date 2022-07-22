

number = int(input())
correct = input()

Adrain = 'ABC'*number 
Bruno = 'BABC'* number 
Goran = 'CCAABB' * number

correct_a = 0
count = 0
for a, b in zip(Adrain, correct):
    count += 1
    if a == b:
        correct_a += 1
    if count == len(correct):
        break
# print(correct_a)

##############
correct_b = 0
count = 0
for a, b in zip(Bruno, correct):
    count += 1
    if a == b:
        correct_b += 1
    if count == len(correct):
        break
# print(correct_b)
##########
correct_g = 0
count = 0
for a, b in zip(Goran, correct):
    count += 1
    if a == b:
        correct_g += 1
    if count == len(correct):
        break
# print(correct_g)

list_c = [correct_a,correct_b,correct_g]
print(max(list_c))
if correct_a > correct_b and correct_a > correct_g:
    print('Adrian')

elif correct_b > correct_a and correct_b > correct_g:
    print('Bruno')
elif correct_g > correct_a and correct_g > correct_b:
    print('Goran')
elif correct_a == correct_b and correct_a > correct_g:
    print('Adrian\nBruno')
elif correct_a == correct_g and correct_a > correct_b:
    print('Adrian\nGoran')
elif correct_b == correct_g and correct_b > correct_a:
    print('Bruno\nGoran')
elif correct_a == correct_b and correct_b == correct_g and correct_a == correct_g:
    print('Adrian')
    print('Bruno')
    print('Goran')

