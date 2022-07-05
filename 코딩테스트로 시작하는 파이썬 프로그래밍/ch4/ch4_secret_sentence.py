sentence = input()
i = 0
print(sentence[i])
result =""
for word in sentence:
    print(word)
    if word in 'aeiou':
        result = result + sentence[i]
        i = i + 3
        print('ok')
    else:
        result = result + sentence[i]
        i = i + 1

print(result)