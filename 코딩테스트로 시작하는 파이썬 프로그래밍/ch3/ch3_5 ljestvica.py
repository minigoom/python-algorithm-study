
mus = input().split('|')
# print(mus)
mus_list = [] # 분리하여 장조 앞자리 담는 리스트이다
for i in mus:
    front = i[0]
    mus_list.append(front)
# print(mus_list)
# print(mus_list[-1])

a_count = 0
c_count = 0
for i in mus_list:
    if i in ['A','D','E']:
        a_count = a_count + 1
    elif i in ['C','F','G']:
        # print('c_출력')
        c_count = c_count + 1
    
if a_count == c_count:
    if mus_list[-1] == 'A':
        a_count = a_count + 1
    elif mus_list[-1] == 'C':
        c_count = c_count + 1
# print(a_count, c_count)
if a_count > c_count:
    print('A-mol')
elif a_count < c_count:
    print('C-dur')

    # print(last)
    # print(type(last))
    # if last == 'A':
    #     print('A-mol')
    # elif last =='C':
    #     print("C-dur")
    