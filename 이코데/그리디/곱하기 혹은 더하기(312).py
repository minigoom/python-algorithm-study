# P312 곱하기 혹은 더하기
# 곱하거나 더하는 두개의 수 중 한개라도 1이하라면 더하기, 그 외에는 곱하기 진행
num = (input())
result = int(num[0])


for i in range(1,len(num)):
    if int(num[i]) <= 1 or result <= 1:
        result = result + int(num[i])
    else:
        result = result * int(num[i])

print(result)