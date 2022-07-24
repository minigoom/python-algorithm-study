n = int(input())
dollar = {1:100, 2:500, 3:1000, 4:5000, 5:10000, 6:25000, 7:50000,8:100000,9:500000,10:1000000}
for i in range(n):
    num = int(input())
    dollar.pop(num)
    # print(dollar)
compare = int(input())
dollar = dollar.values()
# print(dollar)
# print('type:',type(dollar))
if compare > (sum(dollar)/len(dollar)):
    print('deal')

else:
    print('no deal')