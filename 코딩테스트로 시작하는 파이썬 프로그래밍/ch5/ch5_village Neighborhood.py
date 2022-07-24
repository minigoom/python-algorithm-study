# ccc18s1
n = int(input())
x_list = []
for i in range(n):
    x = int(input())
    
    x_list.append(x)
x_list = sorted(x_list) 
bet_list = []  
for i in range(n-1):
    bet = (x_list[i+1] + x_list[i])/2
    bet_list.append(bet)
# print(bet_list)
# print(min(bet_list))
minus_list = []
for i in range(n-2):
    minus = bet_list[i+1] - bet_list[i]
    minus_list.append(minus)
# print(minus_list)
# print(min(minus_list))
result = min(minus_list)
print(result)
