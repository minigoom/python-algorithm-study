sentence = input()
result = ''
for index, i in enumerate(sentence):
    print(index, i)
    if i in ['a','e','i','o','u']:
        result = result + sentence[index]
print(result)       


# for문으로 접근이 불가하다
# while 문을 사용해야한다
# 특정 문자열을 넘기는 문제