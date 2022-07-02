x = input()
smile_count = x.count(':-)')
sad_count = x.count(':-(')
print(smile_count)
print(sad_count)
if smile_count > sad_count:
    print('happy')
elif smile_count != 0 and smile_count == sad_count:
    print('unsure')
elif smile_count < sad_count:
    print('sad')
else:
    print('none')