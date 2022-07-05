songs = 'ABCDE'
# print(songs)
bottom = 0
while bottom != 4:
    # print('시작')
    bottom = int(input())
    num = int(input())
    for i in range(num):
        if bottom == 1:
            songs = songs[1:] + songs[0]
            # print(songs)
        elif bottom == 2:
            songs = songs[-1] + songs[:4]
            # print(songs)
        elif bottom == 3:
            songs = songs[1] + songs[0] + songs[2:]
            # print(songs)


output = ''# 빈 문자열
for song in songs:
    output = output + song + ' '

print(output[:-1])