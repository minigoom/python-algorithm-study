

sentence = input()
# word_position = HONI 
# word_position == 0, H 
# word_position == 1, O
# word_position == 2, N
# word_position == 3, I
match_position = 0
total = 0
for word in sentence:
    if match_position == 0:
        match = 'H'
    elif match_position == 1:
        match = 'O'
    elif match_position == 2:
        match = 'N'
    elif match_position == 3:
        match = 'I'
    print('match_postion:{},match:{},word:{}'.format(match_position, match,word))
    if match == word:
        match_position = match_position+1
        if match_position == 4:
            match_position = 0
            total = total + 1
print(total)