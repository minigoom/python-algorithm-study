
playlist = 'ABCDE'
bottom_number = 0
while bottom_number != 4:
    bottom_number = int(input())
    count = int(input())
    for i in range(0,count):
        if bottom_number == 1:
            playlist = playlist[1:] + playlist[0]
            # print(playlist)
        elif bottom_number == 2:
            playlist = playlist[4] + playlist[0:4]
            # print(playlist)
        elif bottom_number == 3:
            playlist = playlist[1] + playlist[0] + playlist[2:]
            # print(playlist)
for i in playlist:
    print(i,end=' ')