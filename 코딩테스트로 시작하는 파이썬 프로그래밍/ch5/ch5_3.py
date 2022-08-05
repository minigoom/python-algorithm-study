# ch5_3

a_n = int(input())
a_time = []
b_time = []
half = 0
time = []
# 질문1: 전반전에 몇점을 획득하는가?
for i in range(a_n):
    a_t = int(input())
    a_time.append(a_t)
    time.append(a_t)
    if a_t < 1440:
        half = half + 1
b_n = int(input())
for i in range(b_n):
    b_t = int(input())
    b_time.append(b_t)
    time.append(b_t)
    if b_t < 1440:
        half = half + 1
print(half)

# 질문2 몇번의 턴어라운드가 생기는가?
turnaround = 0
score = [0,0]
lead = ""
time.sort()
for i in time:
    if i in a_time:
        score[0] = score[0] + 1
        
    else: 
        score[1] = score[1] + 1

    if score[0] > score[1]:
        lead = lead + 'A'
        
    elif score[0] < score[1]:
        lead = lead + 'B'


for i in range(len(lead)-1):
    
    if lead[i] != lead[i+1]:
      
        turnaround = turnaround+1
       

print(turnaround)
