w = int(input())
c = int(input())

if w == 3 and c >=95:
    variable = 'absolutely'
elif w == 1 and c <= 50:
    variable = 'fairly'
else:
    variable = 'very'

print('C.C. is {} satisfied with her pizza.'.format(variable))