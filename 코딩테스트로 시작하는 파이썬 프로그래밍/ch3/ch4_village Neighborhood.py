num = int(input())
village_list = []
for i in range(0,num):
    village = int(input())
    village_list.append(village)

village_list = sorted(village_list)
# print(village_list)
village_length = []
for i in range(1,num-1):

    length_1 = (village_list[i] - village_list[i-1])/2
    length_2 = (village_list[i+1] - village_list[i])/2
    length = (round(length_1 + length_2,1))
    village_length.append(length)
print(min(village_length))
