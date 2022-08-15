# dmoj - ccc18j3
# input: 직선으로 도시 사이의 거리를 주어진다
# ouput: city i 기준으로 city1, city2, city3, city4, city5 거리를 출력한다.(i는 1~5)

city = list(map(int,input().split()))
city.insert(0,0) # - [0, 3, 10, 12, 5]
city[0] = 0
city[1] = city[0] + city[1]
city[2] = city[1] + city[2] 
city[3] = city[2] + city[3] 
city[4] = city[3] + city[4]
# print(f'city:{city}')3 10 12 5
total_lst = []
for i in range(0,5):
    lst = []
    for j in range(0,5):
        length = abs(city[i] - city[j])
        
        lst.append(length)
    total_lst.append(lst)

for i in total_lst:
    for j in i:
        print(j,end=' ')
    print()

