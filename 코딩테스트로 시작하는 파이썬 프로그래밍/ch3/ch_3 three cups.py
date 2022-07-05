count = input()
ball_location = 1
for i in count:
    if i == 'A' and ball_location ==1:
        ball_location = 2
    elif i == 'A' and ball_location == 2:
        ball_location = 1
    elif i == 'B' and ball_location ==2:
        ball_location = 3
    elif i == 'B' and ball_location ==3:
        ball_location = 2
    elif i == 'C' and ball_location == 3:
        ball_location = 1
    elif i == 'C' and ball_location == 1:
        ball_location = 3

print(ball_location)


        