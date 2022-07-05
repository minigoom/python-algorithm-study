sentence = input()
i = 0
result =''
while i<len(sentence):
    if sentence[i] in 'aeiou':
        result = result + sentence[i]
        i = i + 3
    else:
        result = result + sentence[i]
        i = i + 1
print(result)