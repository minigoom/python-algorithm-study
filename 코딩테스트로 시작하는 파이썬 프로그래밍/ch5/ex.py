# Preokret

A,B, time = [], [], []
half, turn_around = 0,0

A_point = int(input())

for i in range(A_point):
  point = int(input())
  if point <= 1440:
    half += 1
  A.append(point)
#   print('A:',A)
  time.append(point)
#   print('time:',time)

B_point = int(input())

for i in range(B_point):
  point = int(input())
  if point <= 1440:
    half += 1
  B.append(point)
#   print('B:',B)
  time.append(point)
#   print('time:',time)

print(half)

if A[0] < B[0]:
  score = [1,0]
  lead = 'A'
else:
  score = [0,1]
  lead = 'B'
print('socre:',score)
time.sort()
for sec in time[1:]:
  if sec in A:
    score[0] += 1
    print('socre:',score)
  else:
    score[1] += 1
    print('socre:',score)
  
  if score[0] > score[1]:
    lead += 'A'
    print('lead:',lead)
  elif score[0] < score[1]:
    lead += 'B'
    print('lead:',lead)

for i in range(len(lead)-1):
  if lead[i] != lead[i+1]:
    turn_around += 1
    print('turn_around:',turn_around)

print(turn_around)