n = int(input())
coin_type = [500,100,50,10]
count = 0
for i in coin_type:
    count = count + n//i
    n = n%i
print(count)