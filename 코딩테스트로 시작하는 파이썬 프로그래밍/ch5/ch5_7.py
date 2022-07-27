n = int(input())

a = input().split()
time_lst = list(map(int,a ))
# print(time_lst)

large = max(time_lst)
large_index = time_lst.index(large)

small = min(time_lst)
small_index = time_lst.index(small)

if large_index < small_index:
    print('unknown')
else:
    a = small_index
    is_sorted = True
    while a < large_index and is_sorted:
        # print('ok')
        if time_lst[a] > time_lst[a+1]:
            # print('time_lst[a]:',time_lst[a])
            # print('time_lst[large]:',time_lst[a+1])
            is_sorted = False
        a += 1
if is_sorted:
    print(max(time_lst)-min(time_lst))
else:
    print('unknown')