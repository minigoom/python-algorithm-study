use = int(input())
month = int(input())

list = []
for i in range(0,month):
    x = int(input())
    list.append(use-x)

print(sum(list) + use)
