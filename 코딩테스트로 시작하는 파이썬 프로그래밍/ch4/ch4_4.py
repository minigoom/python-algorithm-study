num_next = int(input()) # - Take + 1
num_waiting = 0 # - take + 1, SERVE - 1
num_late = 0 # - Take + 1
# CLOSE print(num_late, num_wating, num_next)
# EOF - while 문 종료
x = False
while not x:
    line = input()
    if line == 'EOF':
        x = True

    elif line == 'TAKE':
        num_next += 1
        num_waiting += 1
        num_late += 1
        if num_next == 1000:
            num_next = 1
    
    elif line == 'SERVE':
        num_waiting -= 1
    elif line == 'CLOSE':
        print(num_late, num_waiting, num_next)
        num_late = 0
        num_waiting = 0
    