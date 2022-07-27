n = int(input())
stream_list = []
for i in range(n):
    stream = int(input())
    stream_list.append(stream)
# print('1:',stream_list)
con_num = 0 # 합쳐질지 나눠질지 판단하는 조건
while con_num != 77:
    con_num = int(input())
    if con_num == 99:
        ind_1 = int(input())-1
        ind_1_ratio = int(input())*0.01
        split_1 = stream_list[ind_1]*ind_1_ratio
        split_2 =  stream_list[ind_1]*(1-ind_1_ratio)
        stream_list.insert(ind_1,split_1)
        # print('split_1:',stream_list)
        stream_list.insert(ind_1+1, split_2)
        # print('split_2:',stream_list)
        stream_list.pop(ind_1+2)
        # print('split_3:',stream_list)


    elif con_num == 88:
        ind = int(input())-1
        join = stream_list[ind] + stream_list[ind+1]
        stream_list[ind] = join
        # print('jon_1',stream_list)
        stream_list.pop(ind+1)
        # print('jon_2',stream_list)

  
for i in stream_list:
            print(i,end=' ')           

