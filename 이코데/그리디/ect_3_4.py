# 이코테 P99
# 1이 될때 까지
# 1. N이 K로 나눠 지는지 아닌지 판단하기
# 2. 반복하는 코드 짜기

N, K = map(int,input().split())
count = 0
# print('ok1')
while N != 1:
    if N % K == 0:
        count += 1
        N = N / K
        # print('ok2')
    else:
        N = N - 1
        count += 1
        # print('ok3')
print(count)

########################
# - 시간 복잡도를 더 좋게 구현하는 방법
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n = n - 1
        result = result + 1
    n = n // K
    result = result + 1

while n > 1:
    n = n - 1
    result = result + 1
print(result)
