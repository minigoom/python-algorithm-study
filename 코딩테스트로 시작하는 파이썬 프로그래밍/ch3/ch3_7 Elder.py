win = input()
count = int(input())
obey = [win]
for i in range(count):
    x ,y = input().split()
    if y == win:
        win = x
        
        obey.append(win)
        obey = list(set(obey))
       
print(win)
print(len(obey))
# print(obey)


