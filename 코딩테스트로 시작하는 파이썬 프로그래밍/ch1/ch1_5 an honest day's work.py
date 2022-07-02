p = int(input())
b = int(input())
d = int(input())
bottle_cap = p//b
left_paint = p%b
total = bottle_cap * d + left_paint
print(total)